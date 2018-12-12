from edc_base.utils import get_utcnow
from edc_constants.constants import YES, FEMALE, POS, NOT_APPLICABLE
from faker import Faker
from model_mommy.recipe import Recipe

from .constants import ABLE_TO_PARTICIPATE
from .models import SubjectScreening


fake = Faker()

subjecteligibility = Recipe(
    SubjectScreening,
    report_datetime=get_utcnow,
    cancer_status=YES,
)
