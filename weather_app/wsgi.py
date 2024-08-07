"""
WSGI config for weather_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# if os.environ.get('DJANGO_SETTINGS_MODULE') == 'weather_app.settings.prod':
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#                           'weather_app.settings.prod')

# else:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings.dev')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings.prod')

application = get_wsgi_application()
