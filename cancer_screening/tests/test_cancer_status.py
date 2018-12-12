from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..eligibility import CancerStatusEvaluator, Eligibility


@tag('test_cancer_status')
class TestCancerStatus(TestCase):

    def test_eligible_cancer_status(self):
        cancer_status_evaluator = CancerStatusEvaluator(has_diagnosis=YES)
        self.assertTrue(cancer_status_evaluator.eligible)
        self.assertEqual(None, cancer_status_evaluator.reason)

    def test_ineligible_cancer_status(self):
        cancer_status_evaluator = CancerStatusEvaluator(has_diagnosis=NO)
        self.assertFalse(cancer_status_evaluator.eligible)
        self.assertIn('Participant Does not Have Cancer.',
                      cancer_status_evaluator.reason)

    def test_eligibility_ok(self):
        eligibility = Eligibility(has_diagnosis=YES)
        self.assertTrue(eligibility.eligible)
        self.assertEqual([], eligibility.reasons)

    def test_ineligibile(self):
        eligibility = Eligibility(has_diagnosis=NO)
        self.assertFalse(eligibility.eligible)
        self.assertIn('Participant Does not Have Cancer.',
                      eligibility.reasons)
