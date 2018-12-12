from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import NO

from ..forms import SubjectScreeningForm


@tag('tsf')
class TestSubjectScreeningForm(TestCase):
    """Testing subject screening form
    """

    def setUp(self):
        self.screening_data = dict(
            screening_identifier='12345',
            subject_identifier='363527',
            report_datetime=get_utcnow(),
            has_diagnosis=NO,
            enrollment_site='gaborone_private_hospital',
            reasons_ineligible={'None'})

    def test_default_ok(self):
        """test if the form is answered correctly as intended, with no errors
        """
        form = SubjectScreeningForm(data=self.screening_data)
        form.is_valid()
        self.assertEqual(form.errors, {})
        self.assertTrue(form.save())

    def test_cancer_status_not_answered(self):
        form = SubjectScreeningForm(data=dict(
            screening_identifier='12345',
            subject_identifier='363527',
            has_diagnosis=None,
            report_datetime=get_utcnow(),
            enrollment_site='gaborone_private_hospital',
            reasons_ineligible={'None'}))
        form.is_valid()
        self.assertEqual(
            form.errors, {'has_diagnosis': ['This field is required.']})
