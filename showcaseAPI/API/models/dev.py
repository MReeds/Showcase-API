from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Developer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = (F('user.date_joined').asc(nulls_last=True),)