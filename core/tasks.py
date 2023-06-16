from celery import shared_task
from .models import Subscriber
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active=True).values_list('email',flat=True)
    mail_text = f"Hello, <br> This is a test mail. <br> Thanks, <br> <h1>Admin</h1>"

    msg = EmailMultiAlternatives(subject='Test subject', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()


send_mail_to_subscribers.delay()

# sleep 10 seconds
import time
@shared_task
def process():
    time.sleep(10)
    return "Hello World"

# process.delay()