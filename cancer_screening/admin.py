from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from simple_history.admin import SimpleHistoryAdmin


from .admin_site import cancer_screening_admin
from .forms import SubjectEligibilityForm
from .models.subject_eligibility import SubjectEligibility
from edc_model_admin.model_admin_audit_fields_mixin import audit_fieldset_tuple


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(SubjectEligibility, site=cancer_screening_admin)
class SubjectEligibilityAdmin(ModelAdminMixin,
                              SimpleHistoryAdmin, admin.ModelAdmin):

    form = SubjectEligibilityForm

    instructions = ['This form is a tool to assist the '
                    'Interviewer to confirm the Eligibility status of the '
                    'subject. After entering the required items, click SAVE.']

#     fieldsets = (
#         (None, {
#             'fields': (
#                 'report_datetime',
#                 "cancer_status",
#                 'enrollment_site',
#                 audit_fieldset_tuple)}))

    list_display = (
        'report_datetime', 'gender')

#     list_filter = ('gender', 'is_eligible', 'is_consented',
#                    'is_refused', 'report_datetime', 'map_area')

    radio_fields = {
        #         'has_identity': admin.VERTICAL,
        #         "gender": admin.VERTICAL,
        #         "citizen": admin.VERTICAL,
        #         "legal_marriage": admin.VERTICAL,
        #         "marriage_certificate": admin.VERTICAL,
        #         "literacy": admin.VERTICAL,
        #         "guardian": admin.VERTICAL,
        #         "inability_to_participate": admin.VERTICAL,
        "cancer_status": admin.VERTICAL,
        "enrollment_site": admin.VERTICAL,
    }

    search_fields = (
        'first_name',
        'initials',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
