from django.test import TestCase, tag
from edc_constants.constants import YES

from ..eligibility import AgeEvaluator


@tag('test_age_evaluator')
class TestAgeEvaluator(TestCase):

    def test_eligible_age_less_than_adult_upper(self):
        age_evaluator = AgeEvaluator(age=18)
        self.assertTrue(age_evaluator.eligible)

    def test_eligible_age_less_than_minor_upper_and_guardian_present(self):
        age_evaluator = AgeEvaluator(age=17, guardian=YES)
        self.assertTrue(age_evaluator.eligible)

    def test_eligible_age_greater_adult_lower(self):
        age_evaluator = AgeEvaluator(age=20)
        self.assertTrue(age_evaluator)

    def test_ineligible_age_less_than_minor_lower(self):
        age_evaluator = AgeEvaluator(age=17)
        self.assertFalse(age_evaluator.eligible)

    def test_ineligible_age_less_than_minor_lower_with_guardian_present(self):
        age_evaluator = AgeEvaluator(age=15, guardian=YES)
        self.assertFalse(age_evaluator.eligible)

    def test_ineligible_age_greater_adult_upper(self):
        age_evaluator = AgeEvaluator(age=65)
        self.assertFalse(age_evaluator.eligible)
