from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Cancer'
    site_header = 'Cancer'
    index_title = 'Cancer'
    site_url = '/cancer_screening_admin/list/'


cancer_screening_admin = AdminSite(name='cancer_screening_admin')
