from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from ..eligibility import LiteracyEvaluator


@tag('test_literacy_evaluator')
class TestLiteracyEvaluator(TestCase):

    def test_eligible_literacy(self):
        literacy_evaluator = LiteracyEvaluator(literate=YES)
        self.assertTrue(literacy_evaluator.eligible)

    def test_ineligible_literacy(self):
        literacy_evaluator = LiteracyEvaluator(literate=NO, guardian=NO)
        self.assertFalse(literacy_evaluator.eligible)
        self.assertEqual('Illiterate with no literate witness.',
                         literacy_evaluator.reason)
