from django.test import TestCase, tag
from edc_constants.constants import YES, NO
from ..eligibility import LiteracyEvaluator
from copy import copy


@tag('test_literacy_evaluator')
class TestLiteracyEvaluator(TestCase):
    pass