from django import forms
from edc_form_validators import FormValidatorMixin
from cancer_screening.models.subject_eligibility import SubjectEligibility


class SubjectEligibilityForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = SubjectEligibility
        fields = '__all__'
