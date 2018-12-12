import re
from uuid import uuid4

from django.core.validators import RegexValidator, MinLengthValidator,\
    MaxLengthValidator
from django.db import models
from django_crypto_fields.fields.firstname_field import FirstnameField
from edc_base.model_managers import HistoricalRecords
from edc_base.sites import CurrentSiteManager, SiteModelMixin

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO, YES_NO_NA, NO, YES,\
    GENDER_UNDETERMINED, YES_NO_UNKNOWN
from edc_constants.constants import UUID_PATTERN, NOT_APPLICABLE
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin

from cancer_screening.choices import INABILITY_TO_PARTICIPATE_REASON,\
    ENROLLMENT_SITES
from cancer_screening.managers import SubjectScreeningManager

from ..eligibility import Eligibility
from ..eligibility_identifier import EligibilityIdentifier


class SubjectIdentifierModelMixin(NonUniqueSubjectIdentifierModelMixin,
                                  models.Model):

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
        elif re.match(UUID_PATTERN, self.subject_identifier):
            pass
        return self.subject_identifier

    def make_new_identifier(self):
        return self.subject_identifier_as_pk.hex

    class Meta:
        abstract = True


class SubjectScreening(SubjectIdentifierModelMixin, SiteModelMixin, BaseUuidModel):

    reference = models.UUIDField(
        verbose_name="Reference",
        unique=True,
        default=uuid4,
        editable=False)

    screening_identifier = models.CharField(
        verbose_name='Eligibility Id',
        max_length=50,
        blank=True,
        unique=True,
        editable=False,
        null=True)

    report_datetime = models.DateTimeField(
        verbose_name='Today\'s date',
        default=get_utcnow,
        validators=[datetime_not_future])

    cancer_status = models.CharField(
        verbose_name="Has a cancer diagnosis been documented?",
        max_length=30,
        choices=YES_NO,
        help_text='If NO, participant is not eligible.'
    )

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    eligible = models.BooleanField(
        default=False,
        editable=False)

    reasons_ineligible = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    on_site = CurrentSiteManager()

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.verify_eligibility()
        if not self.id:
            self.screening_identifier = EligibilityIdentifier().identifier
            self.update_subject_identifier_on_save()
        eligibility = Eligibility(
            cancer_status=self.cancer_status)
        self.is_eligible = eligibility.eligible
        self.loss_reason = eligibility.reasons
        self.registration_identifier = self.screening_identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.screening_identifier} {self.first_name}\
                    ({self.initials}) {self.gender}/{self.age_in_years}'

    def natural_key(self):
        return (self.screening_identifier,)

    def verify_eligibility(self):
        """Verifies eligibility criteria and sets model attrs.
        """
        def if_yes(value):
            return True if value == YES else False

        def if_no(value):
            return True if value == NO else False

        eligibility = Eligibility(
            cancer_status=if_yes(self.cancer_status))
        self.reasons_ineligible = ','.join(eligibility.reasons)
        self.eligible = eligibility.eligible

    class Meta:
        app_label = 'cancer_screening'
        verbose_name = 'Subject Eligibility'
