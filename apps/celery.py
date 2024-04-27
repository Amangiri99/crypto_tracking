import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apps.settings')
app = Celery('apps')
app.config_from_object('django.conf:settings')

# autodiscover tasks present in tasks.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
