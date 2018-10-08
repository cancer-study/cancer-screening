from django.conf import settings
from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'cancer_screening'
    listboard_template_name = 'cancer_screening/listboard.html'
    dashboard_template_name = 'cancer_screening/dashboard.html'
    base_template_name = 'cancer/base.html'
    template_name = 'cancer_screening/home.html'
    listboard_url_name = 'cancer_screening:listboard_url'
    dashboard_url_name = 'cancer_screening/dashboard_url'
    admin_site_name = 'cancer_screening_admin'
    url_namespace = 'cancer_screening'
    eligibility_age_adult_lower = 18
    eligibility_age_adult_upper = 64
    eligibility_age_minor_lower = 16
    eligibility_age_minor_upper = 17


if settings.APP_NAME == 'td_maternal':
    from datetime import datetime
    from dateutil.tz import gettz

    from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
    from edc_base.utils import get_utcnow
    from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
    from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '045'

    class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
        use_settings = True
        device_id = settings.DEVICE_ID
        device_role = settings.DEVICE_ROLE

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP045'
        protocol_number = '045'
        protocol_name = 'Cancer Study'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcBaseAppConfig(BaseEdcBaseAppConfig):
        project_name = 'Cancer Screening'
        institution = 'Botswana-Harvard AIDS Institute'
        copyright = '2013-{}'.format(get_utcnow().year)
        license = None
