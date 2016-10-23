"""Settings for Silent Auction Demo"""
import os
import uuid

gettext = lambda s: s  # noqa

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__), 'demo.db')
    }
}

TIME_ZONE = 'UTC'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

SECRET_KEY = str(uuid.uuid4())

USE_TZ = True
USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('de', gettext('German')),
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('nl', gettext('Nederlands')),
]

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
    'parler',
    'rest_framework',
    'rest_framework.authtoken',
    'silent_auction',
    'versatileimagefield',
)


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


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

# ------------------------------------------------------------------------------
# TRANSLATION Configuration
# ------------------------------------------------------------------------------
PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
PARLER_LANGUAGES = {
    None: (
        {'code': 'de',},
        {'code': 'en',},
        {'code': 'fr',},
        {'code': 'nl',},
    ),
    'default': {
        'fallbacks': [LANGUAGE_CODE],
        'hide_untranslated': False,
    }
}

VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'item_image': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
        ('medium_square_crop', 'crop__400x400'),
        ('small_square_crop', 'crop__50x50')
    ]
}