from django.db import models

# Create your models here.
class student(models.Model):
    subject=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.CharField(max_length=100)
    