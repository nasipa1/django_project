import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project path
sys.path.append('/home/nasipa/django_project')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
