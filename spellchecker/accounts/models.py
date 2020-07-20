from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# # Create your models here.

class User(AbstractUser):
    dob  = models.DateField(null = True, blank = True)
    location = models.CharField(max_length=256, blank = True)
    REQUIRED_FIELDS = ['email']
#custom User Model
# class Profile(models.Model):
#     user =  models.OneToOneField(User, on_delete=models.CASCADE)
#     dob  = models.DateField(null = True, blank = True)
#     location = models.CharField(max_length=256, blank = True)
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()