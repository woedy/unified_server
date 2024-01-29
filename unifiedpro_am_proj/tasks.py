from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings

@shared_task
def send_player_invite_email(subject, content, client_email):
    client_email = EmailMessage(
        subject,
        content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[client_email]
    )
    client_email.send()

