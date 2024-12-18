from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class student(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=50)


