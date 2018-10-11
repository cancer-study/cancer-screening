from django import forms
from edc_form_validators import FormValidatorMixin
from cancer_screening.models import SubjectScreening
from ..form_validator import SubjectScreeningFormValidator


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
