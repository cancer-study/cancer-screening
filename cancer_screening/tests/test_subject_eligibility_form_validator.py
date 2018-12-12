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
            cancer_status=NO,
            enrollment_site='gaborone_private_hospital',
            reasons_ineligible={'None'})
