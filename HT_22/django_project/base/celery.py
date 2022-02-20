import sys
from celery import Celery
from os import path, environ
import django

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

celery_app = Celery('base', broker='pyamqp://guest@localhost/')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()
