from copy import copy
from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from ..eligibility import CitizenshipEvaluator


@tag('test_citizen_evaluator')
class TestCitizenEvaluator(TestCase):

    def setUp(self):
        self.criteria = dict(
            citizen=YES,
            legal_marriage=NO,
            marriage_certificate=NO)

    def test_eligible_citizen(self):
        citizen_evaluator = CitizenshipEvaluator(**self.criteria)
        self.assertTrue(citizen_evaluator.eligible)
        criteria = copy(self.criteria)
        criteria.update(citizen=NO, legal_marriage=YES,
                        marriage_certificate=YES)
        citizen_evaluator = CitizenshipEvaluator(**criteria)
        self.assertTrue(citizen_evaluator.eligible)

    def test_ineligible_citizen(self):
        criteria = copy(self.criteria)
        criteria.update(citizen=NO, legal_marriage=NO,
                        marriage_certificate=NO)
        citizen_evaluator = CitizenshipEvaluator(**criteria)
        self.assertFalse(citizen_evaluator.eligible)
        self.assertEqual('Not a citizen and not married to a citizen..',
                         citizen_evaluator.reason)
        print(citizen_evaluator.reason)

    def test_ineligible_citizen_with_no_marriage_certificate(self):
        criteria = copy(self.criteria)
        criteria.update(citizen=NO, legal_marriage=YES,
                        marriage_certificate=NO)
        citizen_evaluator = CitizenshipEvaluator(**criteria)
        self.assertFalse(citizen_evaluator.eligible)
        self.assertEqual('Not a citizen, married to a citizen but does'
                         ' not have a marriage certificate.',
                         citizen_evaluator.reason)
