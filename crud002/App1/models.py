from django.db import models

# Create your models here.
class Myclass(models.Model):
    username=models.CharField(max_length=50)

    