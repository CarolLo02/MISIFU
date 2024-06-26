"""
ASGI config for misifu project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
#settings_module = 'misifu.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'misifu.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misifu.settings')

application = get_asgi_application()
