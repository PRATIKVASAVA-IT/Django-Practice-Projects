
# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import usermanager


class CustomeUser(AbstractUser):
    mobile=models.IntegerField(unique=True)
    profile_pic=models.ImageField(upload_to='upload',default=None,blank=True,null=True)
    created_at=models.DateTimeField(auto_now=True)
    is_varifid=models.BooleanField(default=False)

    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS=[]
    objects=usermanager()
    
    


   