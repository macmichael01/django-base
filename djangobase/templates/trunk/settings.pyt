# Django project settings for {{ HOSTNAME }}
import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Webmaster', 'webmaster@{{ HOSTNAME }}'),
)

MANAGERS = ADMINS

SITE_ID = 1
SITE_NAME = "{{ PROJECT }}"
SITE_URL = 'http://{{ HOSTNAME }}'
SITE_ROOT = os.path.abspath(os.path.dirname(__file__))

INTERNAL_IPS = ('127.0.0.1',)
HOSTNAME = '{{ HOSTNAME }}'

EMAIL_DEBUG = DEBUG
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.{{ HOSTNAME }}'
EMAIL_HOST_USER = 'webmaster@{{ HOSTNAME }}'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25

DEFAULT_FROM_EMAIL = '"Webmaster" <Webmaster@{{ HOSTNAME }}>'
SERVER_EMAIL = '"Webmaster" <Webmaster@{{ HOSTNAME }}>'

DATABASES = {
    'default': {
        # 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'
        'ENGINE': 'django.db.backends.{{ DATABASE }}',
        'NAME': '{{ PROJECT }}',
        'USER': '{{ PROJECT }}',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ SECRET }}'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
{% if VERSION >= 1.4 %}
# Django timezone-aware datetimes.
USE_TZ = True{% endif %}

USE_ETAGS = True

MEDIA_ROOT = os.path.join(SITE_ROOT, '../media/')
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''
{% if VERSION == 1.3 %}
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'
{% endif %}
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',{% if VERSION >= 1.4 %}
    'django.middleware.clickjacking.XFrameOptionsMiddleware',{% endif %}
)
{% if VERSION >= 1.4 %}
WSGI_APPLICATION = 'wsgi.application'
{% endif %}
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates/'),
)


INSTALLED_APPS = (
    # Django specific
    'django.contrib.auth',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    # 3rd Party
    # 'compressor',
    # 'south',
    # Project Apps
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,{% if VERSION >= 1.4 %}
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },{% endif %}
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',{% if VERSION >= 1.4 %}
            'filters': ['require_debug_false'],{% endif %}
            'propagate': True,
        },
    }
}

try:
    from settings_local import *
except ImportError:
    pass
