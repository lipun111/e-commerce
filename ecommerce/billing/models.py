from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
# Create your models here.

user = settings.AUTH_USER_MODEL
class BillingProfile(models.Model):
    user        = models.OneToOneField(user, null=True, blank=True, on_delete=models.DO_NOTHING)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    #coustomber_id
    def __str__(self):
        return self.email

#
# def billing_profile_created_reciver(sender,instance,created,*args,**kwargs):
#     if created:
#         print('Actual API Calling')
#         instance.coustomber_id = newID
#         instance.save()

def user_created_reciver(sender,instance,created,*args,**kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)
post_save.connect(user_created_reciver, sender=user)
