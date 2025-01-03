from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    img=models.ImageField(upload_to='avatars', blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)

