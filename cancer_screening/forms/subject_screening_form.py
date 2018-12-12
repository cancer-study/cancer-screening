from django import forms
from edc_form_validators import FormValidatorMixin
from cancer_screening.models import SubjectScreening


class SubjectScreeningForm(FormValidatorMixin, forms.ModelForm):

    class Meta:
        model = SubjectScreening
        fields = '__all__'
