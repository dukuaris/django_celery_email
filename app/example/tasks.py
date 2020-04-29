from celery import shared_task

from django.core.mail import send_mail
from django_celery_email import settings

from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(2)
    send_mail(
        'Celery Task Worked!',
        '이것은 자동 이메일 작동 확인 메일입니다.',
        'dukuaris@naver.com',
        ['dhyoo@educasiainc.com',]
    )

    return None
