from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import cancer_screening_admin
from ..models import SubjectScreening
from ..forms import SubjectScreeningForm


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

    form = SubjectScreeningForm

    instructions = ['This form is a tool to assist the '
                    'Interviewer to confirm the Eligibility status of the '
                    'subject. After entering the required items, click SAVE.']

    list_display = (
        'report_datetime', 'gender')

    radio_fields = {
        "cancer_status": admin.VERTICAL,
        "enrollment_site": admin.VERTICAL,
        "guardian": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "citizen": admin.VERTICAL,
        "legal_marriage": admin.VERTICAL,
        "marriage_certificate": admin.VERTICAL,
        "literacy": admin.VERTICAL,
        "guardian": admin.VERTICAL,
        "inability_to_participate": admin.VERTICAL,
        'has_identity': admin.VERTICAL
    }

    search_fields = (
        'first_name',
        'initials',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
