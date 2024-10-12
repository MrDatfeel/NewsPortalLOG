from celery import Celery
import os
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsPortal.settings')

app = Celery('newsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am':{
        'task': 'news.tasks.weekly_send_email_task',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': ()
    }
}
