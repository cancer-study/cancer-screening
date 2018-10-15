from edc_constants.constants import YES, NO, NOT_APPLICABLE
from edc_form_validators import FormValidator


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        condition = (self.cleaned_data.get('age_in_years') < 18)
        self.applicable_if_true(condition=condition, field='age_in_years',
                                field_required='guardian')

        self.not_applicable_if(NOT_APPLICABLE, NO, field='legal_marriage',
                               field_applicable='marriage_certificate')

        self.not_applicable_if(YES, field='citizen',
                               field_applicable='legal_marriage')

        self.applicable_if(YES, field='legal_marriage',
                           field_required='marriage_certificate')
