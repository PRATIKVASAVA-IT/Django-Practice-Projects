from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from custuser.mangers import usermanager

class mycustomeuser(AbstractUser):
    username=None
    mobile=models.IntegerField(unique=True)
    profile_photo=models.ImageField(upload_to='uploads',default=None,blank=True,null=True)
    is_verified=models.BooleanField(default=False)

    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS=[]

    objects=usermanager()

    def __str__(self):
        return str(self.mobile)
    

class trackermodel(models.Model):
    comment=models.CharField(max_length=100)
    amount=models.FloatField()
    user=models.ForeignKey(mycustomeuser,on_delete=models.CASCADE,null=True, blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)


    
        

    