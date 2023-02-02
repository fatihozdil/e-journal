"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
name = os.environ['DJANGO_SETTINGS_MODULE'] if 'DJANGO_SETTINGS_MODULE' in os.environ else env('DJANGO_SETTINGS_MODULE')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{name}")

application = get_wsgi_application()
