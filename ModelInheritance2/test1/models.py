from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    add1=models.CharField(max_length=100)
    add2=models.CharField(max_length=100)
    add3=models.CharField(max_length=100)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    country=models.CharField(max_length=40)
    pin=models.IntegerField()

class customer(Address):
    
    cust_name=models.CharField(max_length=100,default=True,null=True)

    cust_surname=models.CharField(max_length=100,default=True,null=True)
    
    cust_mobile=models.IntegerField(default=True,null=True)


class run_customer(customer):
    class Meta:
        proxy=True

    
