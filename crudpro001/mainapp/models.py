from django.db import models

# Create your models here.
class UserAdd(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.IntegerField()
    password=models.CharField(max_length=20)

    def __str__(self) :
        return self.name