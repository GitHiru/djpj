import os
from django.core.wsgi import get_wsgi_application


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djpj.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djpj.settings.dev') #edit:
#🔗https://stackoverflow.com/questions/24488891/gunicorn-errors-haltserver-haltserver-worker-failed-to-boot-3-django

application = get_wsgi_application()
