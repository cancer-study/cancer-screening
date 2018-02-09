from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from edc_base.utils import get_uuid
from edc_consent.site_consents import site_consents
from edc_model_wrapper import ModelWrapper
from ..models import SubjectEligibility


class ConsentMixin:

    @property
    def consent_object(self):
        """Returns the consent model.
        """
        default_consent_group = django_apps.get_app_config(
            'edc_consent').default_consent_group
        consent_object = site_consents.get_consent(
            report_datetime=self.object.report_datetime,
            consent_group=default_consent_group)
        return consent_object

    @property
    def consent(self):
        """Returns a wrapped saved or unsaved consent.
        """
        from cancer_subject.views import SubjectConsentModelWrapper
        consent_model_wrapper_class = SubjectConsentModelWrapper
        try:
            consent = self.consent_object.model.objects.get(
                version=self.consent_object.version,
                screening_identifier=self.object.screening_identifier,)
        except ObjectDoesNotExist:
            consent = self.consent_object.model(
                subject_identifier=self.object.subject_identifier,
                consent_identifier=get_uuid(),
                screening_identifier=self.object.screening_identifier,
                version=self.consent_object.version)
            consent = consent_model_wrapper_class(consent)
        if consent:
            consent = consent_model_wrapper_class(consent)
        return consent


class SubjectEligibilityModelWrapper(ConsentMixin, ModelWrapper):

    model = 'cancer_screening.subjecteligibility'
    next_url_name = django_apps.get_app_config(
        'cancer_screening').listboard_template_name
    next_url_attrs = ['screening_identifier']
    querystring_attrs = ['gender']
