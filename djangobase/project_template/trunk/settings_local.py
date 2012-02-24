# Development settings (exclude from production)
import os

# from settings import INSTALLED_APPS

# DEBUG = True
# COMPRESS_ENABLED = False

# TEST EMAIL USING GMAIL
# EMAIL_DEBUG = True
# EMAIL_USE_TLS = True
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_HOST_USER='ACCOUNT@gmail.com'
# EMAIL_HOST_PASSWORD='PASSWORD'
# EMAIL_PORT= 587
# SERVER_EMAIL = "webmaster@gmail.com"

# Testing email locally
# EMAIL_HOST = 'localhost'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 1025
# EMAIL_USE_TLS = False
# Run the following from a terminal window locally.
# python -m smtpd -n -c DebuggingServer localhost:1025

# PATHS
# ADMIN_MEDIA_PREFIX = '/static/admin_media/'
# MEDIA_URL = 'http://localhost/media/'
# STATIC_URL = 'http://localhost/static/'

# MEMCACHE
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }
# 
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake'
#     }
# }

# Non-Production apps here.
# MORE_APPS = (
#     'django_extensions',
# )
# INSTALLED_APPS = INSTALLED_APPS + MORE_APPS
