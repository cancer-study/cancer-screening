from django.db import models


class EligibilityManager(models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(
            subject_eligibility__screening_identifier=screening_identifier
        )
