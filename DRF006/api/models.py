from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    city=models.CharField(max_length=30)


    def __str__(self):
        return self.name