import os
import celery
from decouple import config

from django.conf import settings

from apps.scraper import schedules as scraper_schedules


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")
app = celery.Celery("apps")
# Configure Celery app settings
app.conf.update(
    broker_url=config("BROKER_URL", default="redis://redis:6379/0"),
    task_serializer=config("CELERY_TASK_SERIALIZER", default="json"),
    accept_content=config("CELERY_ACCEPT_CONTENT", default=["application/json"]),
    beat_scheduler=config(
        "CELERY_BEAT_SCHEDULER", "django_celery_beat.schedulers:DatabaseScheduler"
    ),
)

# Define the beat schedule
app.conf.beat_schedule = scraper_schedules.CELERY_BEAT_SCHEDULE

# Autodiscover and register tasks from all installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
