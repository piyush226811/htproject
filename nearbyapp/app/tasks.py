from __future__ import absolute_import
from django.core.mail import send_mail

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def email_24(mail_list_d):

	mail_string = mail_list_h['mail_list'];
	#mail_list = mail_string.split(",");

	send_mail('event reminder', 'your event '+mail_list_h['name']+' starts in 1 hour', 'from@example.com',[mail_string], fail_silently=False)

	return mail_list_d;

@shared_task
def email_1(mail_list_h):

	mail_string = mail_list_h['mail_list'];
	#mail_list = mail_string.split(",");

	send_mail('event reminder', 'your event '+mail_list_h['name']+' starts in 1 hour', 'from@example.com',[mail_string], fail_silently=False)

	return mail_list_h;
