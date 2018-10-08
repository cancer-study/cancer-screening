from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import cancer_screening_admin

app_name = 'cancer_screening'

urlpatterns = [
    path('admin/', cancer_screening_admin.urls),
    path('', RedirectView.as_view(url='/'), name='home_url'),
]
