from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# import randomwhile



class Consumer(models.Model):
    # informations
    email = models.EmailField()
    position = models.CharField(_("Position"), max_length=250)
    position_info = models.TextField(_("Position info"))

    # moderations
    deadline = models.DateTimeField(_("deadline"), auto_now=False, auto_now_add=False)
    secret_key = models.CharField(_("Secret Key"), max_length=2500, blank=True, null= True)
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

    def __str__(self):
        return str(self.email)

    

