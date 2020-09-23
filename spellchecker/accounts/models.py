from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.

class User(AbstractUser):
    dob  = models.DateField(null = True, blank = True)
    company_name =  models.CharField(max_length = 256, blank = True)
    primary_phone_number = models.CharField(max_length = 256, blank = True)  
    designation = models.CharField(max_length = 256, blank = True)
    addressline1  = models.CharField(max_length = 256, blank = True)
    addressline2  = models.CharField(max_length = 256, blank = True)
    city = models.CharField(max_length = 256, blank = True)
    zip_code = models.CharField(max_length = 256, blank = True)
    state = models.CharField(max_length = 256, blank = True)
    country = models.CharField(max_length = 256, blank = True)
    secret_question = models.CharField(max_length = 256, blank = True)
    secret_answer =  models.CharField(max_length = 256, blank = True)
    is_blocked = models.BooleanField(default = False)
    REQUIRED_FIELDS = ['email']
 
