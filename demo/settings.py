"""Settings for Silent Auction Demo"""
import os
import uuid

gettext = lambda s: s

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'demo.db')
    }
}

TIME_ZONE = 'Europe/Paris'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

SECRET_KEY = str(uuid.uuid4())

USE_TZ = False
USE_I18N = False
USE_L10N = False


LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext('English')),
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'taggit',
    'silent-auction'
)