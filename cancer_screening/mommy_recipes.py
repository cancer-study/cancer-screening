from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from faker import Faker
from model_mommy.recipe import Recipe

from .models import SubjectScreening


fake = Faker()

subjectscreening = Recipe(
    SubjectScreening,
    report_datetime=get_utcnow,
    has_diagonis=YES,
)
