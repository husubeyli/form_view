from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'form_view.settings')

# app = Celery('food_stories')
app = Celery('form_view')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request salam: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'everyday-task': {
        'task': 'accounts.tasks.check_for_deadline',
        'schedule': crontab(minute='*/1'),
    },
}
