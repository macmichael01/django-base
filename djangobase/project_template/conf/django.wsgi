import os
import sys
import site

PATH = '/usr/local/projects/{{ PROJECT }}'

# Virtualenv
site.addsitedir('%s/env/lib/python2.6/site-packages' % PATH)

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Project Trunk
sys.path.append('%s/trunk' % PATH)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
