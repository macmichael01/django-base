import os
import sys
import site

PATH = '{{ PROJECTPATH }}'

# Virtualenv
site.addsitedir('%s/env/lib/python2.6/site-packages' % PATH)

# Redirect print statements to apache log
sys.stdout = sys.stderr

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'settings')

# Project Trunk
sys.path.append('%s/{{ PROJECT }}' % PATH)

# Django 1.3
# from django.core.handlers.wsgi import WSGIHandler
# application = WSGIHandler()

# Django 1.4
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
