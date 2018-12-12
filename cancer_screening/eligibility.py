from edc_constants.constants import YES


class CancerStatusEvaluator:

    def __init__(self, cancer_status=None):
        self.eligible = None
        self.reason = None
        if cancer_status == YES:
            self.eligible = True
        else:
            self.eligible = False
            self.reason = 'Participant Does not Have Cancer.'


class Eligibility:

    def __init__(self, cancer_status=None):

        self.cancer_status_evaluator = CancerStatusEvaluator(
            cancer_status=cancer_status)
        self.criteria = dict(
            cancer_status=self.cancer_status_evaluator.eligible
        )
        self.eligible = all(self.criteria.values())

    @property
    def reasons(self):
        """Returns a list of reason not eligible.
        """
        reasons = [k for k, v in self.criteria.items() if not v]
        if self.cancer_status_evaluator.reason:
            reasons.pop(reasons.index('cancer_status'))
            reasons.append(self.cancer_status_evaluator.reason)
        return reasons
