from copy import copy
from django.test import TestCase, tag
from django.core.exceptions import ValidationError
from edc_constants.constants import YES, FEMALE, NO, NOT_APPLICABLE
from edc_base.utils import get_utcnow
from ..constants import ABLE_TO_PARTICIPATE
from ..form_validator import SubjectScreeningFormValidator


@tag('tsfv')
class TestSubjectScreeningFormValidator(TestCase):
    """Testing subject screening form validator
    """

    def setUp(self):
        self.screening_data = dict(
            screening_identifier='12345',
            subject_identifier='363527',
            report_datetime=get_utcnow(),
            gender=FEMALE,
            initials='MM',
            inability_to_participate=ABLE_TO_PARTICIPATE,
            cancer_status=NO,
            enrollment_site='gaborone_private_hospital',
            age_in_years=23,
            guardian=NOT_APPLICABLE,
            citizen=YES,
            has_identity=YES,
            legal_marriage=NOT_APPLICABLE,
            marriage_certificate=NOT_APPLICABLE,
            literacy=YES,
            reasons_ineligible={'None'})

    def test_guardian_field_required_ok(self):
        """test the guardian field required when participant is minor
           raises guardian required error if the participant is minor
           and guardian field is set to not applicable
        """
        current_details = copy(self.screening_data)
        current_details['age_in_years'] = 10
        current_details['guardian'] = NOT_APPLICABLE
        condition = current_details['age_in_years'] < 18
        validator = SubjectScreeningFormValidator(cleaned_data=current_details)
        self.assertRaises(
            ValidationError,
            validator.required_if_true,
            condition=condition, field='age_in_years',
                                       field_required='guardian')

    def test_married_to_citizen_field_applicable_ok(self):
        """test the field legal marriage applicable if the participant
           is not a citizen
        """
        current_details = copy(self.screening_data)
        current_details['citizen'] = YES
        current_details['legal_marriage'] = NO
        validator = SubjectScreeningFormValidator(cleaned_data=current_details)
        self.assertRaises(
            ValidationError,
            validator.applicable_if,
            NO, field='citizen',
            field_applicable='legal_marriage')

    def test_married_to_citizen_field_not_applicable_ok(self):
        current_details = copy(self.screening_data)
        current_details['legal_marriage'] = YES
        validator = SubjectScreeningFormValidator(cleaned_data=current_details)
        self.assertRaises(
            ValidationError,
            validator.not_applicable_if,
            YES, field='citizen',
            field_applicable='legal_marriage')

    def test_marriage_certificate_not_applicable_ok(self):
        current_details = copy(self.screening_data)
        current_details['legal_marriage'] = NO
        current_details['marriage_certificate'] = NO
        validator = SubjectScreeningFormValidator(cleaned_data=current_details)
        self.assertRaises(
            ValidationError,
            validator.not_applicable_if,
            NO, field='legal_marriage',
            field_applicable='marriage_certificate')

    def test_marriage_certificate_applicable_ok(self):
        current_details = copy(self.screening_data)
        current_details['legal_marriage'] = YES
        validator = SubjectScreeningFormValidator(cleaned_data=current_details)
        self.assertRaises(
            ValidationError,
            validator.applicable_if,
            YES, field='legal_marriage',
            field_applicable='marriage_certificate')

    def test_not_married_to_citizen_no_certificate(self):
        self.screening_data['citizen'] = NO
        self.screening_data['legal_marriage'] = NOT_APPLICABLE
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=self.screening_data)
        self.assertRaises(ValidationError, form_validator.validate)

    def test_not_minor_guardian(self):
        self.screening_data['age_in_years'] = 18
        self.screening_data['guardian'] = YES
        form_validator = SubjectScreeningFormValidator(
            cleaned_data=self.screening_data)
        self.assertRaises(ValidationError, form_validator.validate)
