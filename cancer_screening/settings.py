"""
Django settings for bcpp_clinic project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import configparser
import os
from pathlib import PurePath
import sys

from django.core.management.color import color_style


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

style = color_style()

APP_NAME = 'cancer_screening'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*3izpxc9!j7)(a*2+_sw%_10gx*_$z1-%bf2mz%!pkd%@*%$1)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CONFIG_FILE = '{}.conf'.format(APP_NAME)
if DEBUG:
    ETC_DIR = str(PurePath(BASE_DIR).joinpath('etc'))
else:
    ETC_DIR = '/etc'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CONFIG_PATH = os.path.join(ETC_DIR, APP_NAME, CONFIG_FILE)
sys.stdout.write(style.SUCCESS('Reading config from {}\n'.format(CONFIG_PATH)))

config = configparser.RawConfigParser()
config.read(os.path.join(CONFIG_PATH))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_nose',
    'tz_detect',
    'rest_framework',
    'rest_framework.authtoken',
    'django_crypto_fields.apps.AppConfig',
    'django_revision.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_protocol.apps.AppConfig',
    'cancer_screening.apps.AppConfig',
]


# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
]

if 'test' in sys.argv:
    MIGRATION_MODULES = {
        "django_crypto_fields": None,
        'edc_identifier': None,
        'cancer_screening': None,
        'edc_device': None,
        'django_revision': None,
        'edc_protocol': None,
        'admin': None,
        "auth": None,
        'sessions': None,
    }

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cancer_screening.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cancer_screening.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME':
     'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
     },
    {'NAME':
     'django.contrib.auth.password_validation.MinimumLengthValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.CommonPasswordValidator',
     },
    {'NAME':
     'django.contrib.auth.password_validation.NumericPasswordValidator',
     },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, APP_NAME, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, APP_NAME, 'media')

MEDIA_URL = '/media/'

GIT_DIR = BASE_DIR


DEVICE_ID = '21'
DEVICE_ROLE = 'Client'
LABEL_PRINTER = 'label_printer'
