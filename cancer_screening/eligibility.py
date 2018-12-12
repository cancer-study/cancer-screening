from edc_constants.constants import YES


class CancerStatusEvaluator:

    def __init__(self, has_diagnosis=None):
        self.eligible = None
        self.reason = None
        if has_diagnosis == YES:
            self.eligible = True
            self.reason = None
        else:
            self.eligible = False
            self.reason = 'Participant Does not Have Cancer.'


class Eligibility:

    def __init__(self, has_diagnosis=None):

        self.cancer_status_evaluator = CancerStatusEvaluator(
            has_diagnosis=has_diagnosis)
        self.criteria = dict(
            has_diagnosis=self.cancer_status_evaluator.eligible
        )
        self.eligible = all(self.criteria.values())

    @property
    def reasons(self):
        """Returns a list of reason not eligible.
        """
        reasons = [k for k, v in self.criteria.items() if not v]
        if self.cancer_status_evaluator.reason:
            reasons.pop(reasons.index('has_diagnosis'))
            reasons.append(self.cancer_status_evaluator.reason)
        return reasons
