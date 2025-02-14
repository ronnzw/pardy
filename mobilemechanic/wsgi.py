"""
WSGI config for mobilemechanic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# importing whitenoise
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.prod')

application = get_wsgi_application()

# wrapping up existing wsgi application
application = WhiteNoise(application, root="staticfiles")
