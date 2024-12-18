from django.db import models

# Create your models here.

class Address(models.Model):
    add1=models.CharField(max_length=80)
    add2=models.CharField(max_length=80)
    city=models.CharField(max_length=50)
    dis=models.CharField(max_length=40)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
class customer(Address):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    email=models.EmailField()

class Profile(customer):
    date=models.DateField(auto_now_add=True)

    
