import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education_platform_for_pythoneers.settings")

application = get_asgi_application()
