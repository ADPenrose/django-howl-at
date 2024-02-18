"""
WSGI config for vercel_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vercel_app.settings")

# If we are on prouction, we need to tell vercel to import files from
# the parent directory of this file, and not the base directory.
if os.environ.get("ENV") == "production":
    print("Production environment detected")
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
else:
    print("Development environment detected")

app = get_wsgi_application()
