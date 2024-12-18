from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class Login_customer(models.Model):
    uname=models.CharField(max_length=40,default=True,null=True)

    password=models.CharField(max_length=40,default=True,null=True)