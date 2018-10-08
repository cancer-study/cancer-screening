from django.apps import apps as django_apps
from django.db.models.constants import LOOKUP_SEP

from edc_device.constants import CLIENT, SERVER, NODE_SERVER
from edc_map.site_mappers import site_mappers


class MapAreaQuerysetViewMixin:

    subject_queryset_lookups = []

    @property
    def subject_lookup_prefix(self):
        subject_lookup_prefix = LOOKUP_SEP.join(self.subject_queryset_lookups)
        return '{}__'.format(subject_lookup_prefix)\
            if subject_lookup_prefix else ''

    def add_map_area_filter_options(self, options=None, **kwargs):
        """Updates the filter options to limit the subject returned
        to those in the current map_area.
        """
        map_area = site_mappers.current_map_area
        options.update(
            {'{}map_area'.format(self.subject_lookup_prefix): map_area})
        return options

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        edc_device_app_config = django_apps.get_app_config('edc_device')
        if edc_device_app_config.device_role in [SERVER, CLIENT, NODE_SERVER]:
            options = self.add_map_area_filter_options(
                options=options, **kwargs)
        return options
