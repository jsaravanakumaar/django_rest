"""
WSGI config for django_rest_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_rest_project.settings')
sys.path.append('/home/ubuntu/django/django_rest/')
sys.path.append('/home/ubuntu/django/django_rest/django_rest_project')
sys.path.append('/home/ubuntu/django/django_rest/django_rest_project/django_rest_project')

application = get_wsgi_application()
