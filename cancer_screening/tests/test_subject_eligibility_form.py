from copy import copy
from django.test import TestCase, tag
from django.core.exceptions import ValidationError
from edc_constants.constants import YES, FEMALE, NO, NOT_APPLICABLE
from edc_base.utils import get_utcnow
from ..constants import ABLE_TO_PARTICIPATE
from ..forms import SubjectEligibilityForm


@tag('tsf')
class TestSubjectScreeningForm(TestCase):
    """Testing subject screening form
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

    def test_default_ok(self):
        """test if the form is answered correctly as intended, with no errors
        """
        form = SubjectEligibilityForm(data=self.screening_data)
        form.is_valid()
        self.assertEqual(form.errors, {})
        self.assertTrue(form.save())

    def test_guardian_required(self):
        """test if the age_in_years field value is minor and
        the guardian field is required
        Assert raises guardian field required if the guardian field is
        set to not applicable
        """
        data = copy(self.screening_data)
        data.update(
            age_in_years=8)
        form = SubjectEligibilityForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'guardian':
                          ['This field is required.']})

    def test_guardian_not_required(self):
        """test if the age_in_years field value is not minor and
        the guardian field is not required
        Assert raises guardian field required if the guardian field is
        set to not applicable
        """
        data = copy(self.screening_data)
        data.update(
            age_in_years=18,
            guardian=YES)
        form = SubjectEligibilityForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'guardian':
                          ['This field is not required.']})

    def test_legal_marriage_not_applicable(self):
        """test citizen field set to YES and legal marriage field
          is not applicable
        """
        data = copy(self.screening_data)
        data.update(
            citizen=YES,
            legal_marriage=YES,
            marriage_certificate=YES)
        form = SubjectEligibilityForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'legal_marriage':
                          ['This field is not applicable']})

    def test_marriage_certificate_required(self):
        """test citizen field set to NO and legal marriage field is set to YES
          then marriage_certificate field is missing
          raises marriage_certificate field required
        """
        data = copy(self.screening_data)
        data.update(
            citizen=NO,
            legal_marriage=YES,
            marriage_certificate=NOT_APPLICABLE)
        form = SubjectEligibilityForm(data=data)
        form.is_valid()
        self.assertEqual(
            form.errors, {'marriage_certificate':
                          ['This field is applicable']})
