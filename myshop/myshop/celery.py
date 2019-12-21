import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

celery = Celery('tasks', broker='amqp://zotvmndg:YDHusmUevLm73QV9G7cpYJql_kS1GYU9@jellyfish.rmq.cloudamqp.com/zotvmndg')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()