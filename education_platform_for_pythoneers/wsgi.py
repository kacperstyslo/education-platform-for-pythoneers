import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education_platform_for_pythoneers.settings")
application = get_wsgi_application()
