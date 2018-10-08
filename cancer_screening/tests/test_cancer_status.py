from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..eligibility import CancerStatusEvaluator


@tag('test_cancer_status')
class TestCancerStatus(TestCase):

    def test_eligible_cancer_status(self):
        cancer_status_evaluator = CancerStatusEvaluator(cancer_status=YES)
        self.assertTrue(cancer_status_evaluator.eligible)
        self.assertEqual(None, cancer_status_evaluator.reason)

    def test_ineligible_cancer_status(self):
        cancer_status_evaluator = CancerStatusEvaluator(cancer_status=NO)
        self.assertFalse(cancer_status_evaluator.eligible)
        self.assertIn('Participant Does not Have Cancer.',
                      cancer_status_evaluator.reason)
