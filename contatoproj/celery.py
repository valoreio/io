from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, signals
from kombu import Exchange, Queue
from django.conf import settings
from password_contatoproj import broker_var, backend_var


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contatoproj.settings')

#O zero do redis significa DB Number 
app = Celery('contatoproj',
    broker = broker_var,
    backend = backend_var,
    include = ['contatoapp.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=120,
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERYD_TASK_SOFT_TIME_LIMIT=60,
    #CELERY_SEND_TASK_ERROR_EMAILS=True,
    #ADMINS = (('Eu mesmo', 'x@gmail.com'),),
    CELERY_DEFAULT_QUEUE='contatoapp_queue',
#    CELERY_QUEUES=(
#        Queue('django_project', Exchange('django_project'), routing_key='django_project'),
#    ),
#    CELERY_IGNORE_RESULT=False,
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
