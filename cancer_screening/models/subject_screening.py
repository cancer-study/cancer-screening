from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators.date import datetime_not_future
from edc_base.sites import CurrentSiteManager, SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin

from cancer_screening.choices import ENROLLMENT_SITES
from cancer_screening.managers import SubjectScreeningManager
from cancer_screening.eligibility_identifier import EligibilityIdentifier


class SubjectScreening(
        NonUniqueSubjectIdentifierModelMixin, SiteModelMixin, BaseUuidModel):

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

    has_diagnosis = models.CharField(
        verbose_name="Has a cancer diagnosis been documented? ",
        max_length=3,
        choices=YES_NO,
        help_text="( if 'NO' STOP patient cannot be enrolled )",)

    enrollment_site = models.CharField(
        verbose_name='Enrollment Site',
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    # is updated via signal once subject is consented
    is_consented = models.BooleanField(
        default=False,
        editable=False)

    on_site = CurrentSiteManager()

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.verify_eligibility()
        if not self.id:
            self.screening_identifier = EligibilityIdentifier().identifier
            self.update_subject_identifier_on_save()
        self.registration_identifier = self.screening_identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.screening_identifier} {self.first_name}\
                    ({self.initials}) {self.gender}/{self.age_in_years}'

    def natural_key(self):
        return (self.screening_identifier,)

    class Meta:
        app_label = 'cancer_screening'
        verbose_name = 'Subject Eligibility'
