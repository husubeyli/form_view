import os
import string
import random
from django.db.models.signals import post_save, pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from .models import Consumer


all_ = string.digits+string.ascii_letters


def code_email_generator(size=32, chars=all_):
    return ''.join(random.choice(chars) for _ in range(size))


def create_secret_key(size=32):
    new_code = code_email_generator(size=size)
    qs_exists = Consumer.objects.filter(secret_key=new_code).exists()
    if qs_exists:
        return create_secret_key(size=size)
    return new_code


@receiver(post_save, sender=Consumer)
def create_product(sender, instance, created,  **kwargs):
    if created:
        from .tasks import check_for_deadline
        ran_int = create_secret_key()
        instance.secret_key = ran_int
        send_mail(
            'subject', f'This is you membership id {ran_int}', 'husubayli@gmail.com', [instance.email, ])
        instance.save()
