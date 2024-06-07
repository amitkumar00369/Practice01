# tasks.py

from celery import shared_task
from .utils import reset_google_form_links

@shared_task
def reset_google_form_links_task():
    reset_google_form_links()
