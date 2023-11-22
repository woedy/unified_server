import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unifiedpro_am_proj.settings')
app = Celery('unifiedpro_am_proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()