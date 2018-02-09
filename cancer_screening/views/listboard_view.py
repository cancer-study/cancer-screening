import re

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView

from ..models import SubjectEligibility
from ..view_mixins import MapAreaQuerysetViewMixin
from .wrappers import SubjectEligibilityModelWrapper


class ListBoardView(AppConfigViewMixin, EdcBaseViewMixin, MapAreaQuerysetViewMixin, ListboardView):

    model = 'cancer_screening.subjecteligibility'
    model_wrapper_cls = SubjectEligibilityModelWrapper
    listboard_url_name = django_apps.get_app_config(
        'cancer_screening').listboard_url_name
    paginate_by = 10
    navbar_item_selected = 'cancer_screening'
    app_config_name = 'cancer_screening'
    ordering = '-modified'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('screening_identifier'):
            options.update(
                {'screening_identifier': kwargs.get('screening_identifier')})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
