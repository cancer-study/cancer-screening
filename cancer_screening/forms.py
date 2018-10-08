from django import forms
from edc_form_validators import FormValidatorMixin
from cancer_screening.models.subject_eligibility import SubjectEligibility


class SubjectEligibilityForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = None

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
