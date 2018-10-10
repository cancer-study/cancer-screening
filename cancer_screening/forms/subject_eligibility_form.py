from django import forms
from edc_form_validators import FormValidatorMixin
from cancer_screening.models.subject_eligibility import SubjectEligibility
from ..form_validator import SubjectScreeningFormValidator


class SubjectEligibilityForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
