"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Define the project directory
project_home = '/home/nasipa/django_project'

# Add the project directory to the sys.path
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# Initialize the WSGI application
application = get_wsgi_application()
