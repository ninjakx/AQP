"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print("basdir",BASE_DIR)
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

application = get_wsgi_application()
