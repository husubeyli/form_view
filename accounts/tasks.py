from datetime import datetime
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Consumer

from form_view.celery import app



@app.task()
def check_for_deadline():   
    print('task isleyir')   
    cunsumers = Consumer.objects.all()
    print(timezone.datetime.today(), 'sa')
    print(timezone.now(), 'sa')
    for obj in cunsumers:
        print(obj.deadline, 'qaqa')
        if obj.deadline > timezone.now():
            print('*' * 8)
            send_mail('Manufacturing Reminder', f'This is you membership id {obj.secret_key}', 'husubayli@gmail.com', [obj.email,])
    return None


