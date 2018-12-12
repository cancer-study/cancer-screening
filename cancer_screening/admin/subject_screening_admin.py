from django.conf import settings
from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from simple_history.admin import SimpleHistoryAdmin

from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)

from ..admin_site import cancer_screening_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(SubjectScreening, site=cancer_screening_admin)
class SubjectScreeningAdmin(ModelAdminMixin,
                            SimpleHistoryAdmin, admin.ModelAdmin):

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'screening_dashboard_url')

    form = SubjectScreeningForm

    instructions = ['This form is a tool to assist the '
                    'Interviewer to confirm the Eligibility status of the '
                    'subject. After entering the required items, click SAVE.']

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'has_diagnosis',
                'enrollment_site')
        }),
    )

    radio_fields = {
        'enrollment_site': admin.VERTICAL}

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
