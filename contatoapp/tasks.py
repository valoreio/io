from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

@shared_task(bind=True, default_retry_delay=300, max_retries=10) # Use this decorator to make this a asyncronous function
def save_postview_taskscelery(self, request, reg):

    try:
        reg.save()

    except ConnectionError as exc:
        self.retry(exc=exc, countdown=180)  # the task goes back to the queue


@shared_task(bind=True, default_retry_delay=300, max_retries=10) # Use this decorator to make this a asyncronous function
def send_postview_taskscelery_com(self, request, reg, subject_1, message_1, from_email, subject_2, message_2):

    try:

        # envia o email para avisar o comercial da valore.io
        try:
            send_mail(subject_1, message_1, from_email, [settings.EMAIL_COMERCIAL])
        except BadHeaderError:
            return HttpResponse('Invalid comercial header found.')

    except ConnectionError as exc:
        self.retry(exc=exc, countdown=180)  # the task goes back to the queue


@shared_task(bind=True, default_retry_delay=300, max_retries=10) # Use this decorator to make this a asyncronous function
def send_postview_taskscelery_dir(self, request, reg, subject_1, message_1, from_email, subject_2, message_2):

    try:

        # envia o email para avisar o diretor da valore.io
        try:
            send_mail(subject_1, message_1, from_email, [settings.EMAIL_DIRETOR])
        except BadHeaderError:
            return HttpResponse('Invalid diretor header found.')

    except ConnectionError as exc:
        self.retry(exc=exc, countdown=180)  # the task goes back to the queue


@shared_task(bind=True, default_retry_delay=300, max_retries=10) # Use this decorator to make this a asyncronous function
def send_postview_taskscelery_usu(self, request, reg, subject_1, message_1, from_email, subject_2, message_2):

    try:

        # envia o email para tranquilizar o usuario
        try:
            send_mail(subject_2, message_2, settings.EMAIL_COMERCIAL, [from_email])
        except BadHeaderError:
            return HttpResponse('Invalid usuario header found.')

    except ConnectionError as exc:
        self.retry(exc=exc, countdown=180)  # the task goes back to the queue
