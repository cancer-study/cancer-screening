from django.test import TestCase, tag
from ..constants import ABLE_TO_PARTICIPATE
from ..eligibility import ParticipationEvaluator


@tag('test_participation_evaluator')
class TestParticipationEvaluator(TestCase):

    def test_eligible_participation(self):
        participation_evaluator = ParticipationEvaluator(
            participation=ABLE_TO_PARTICIPATE)
        self.assertTrue(participation_evaluator.eligible)

    def test_ineligible_participation(self):
        participation_evaluator = ParticipationEvaluator()
        self.assertFalse(participation_evaluator.eligible)
        self.assertEqual('Not able participant None.',
                         participation_evaluator.reason)
