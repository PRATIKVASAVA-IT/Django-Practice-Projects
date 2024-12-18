from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post_class(models.Model):
    user=models.ForeignKey(User)
    DateCreated=models.DateTimeField()
    post=models.TextField()
    photo=models.ImageField(default=None,upload_to='/post_images')
    
    