from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(blank=True,null=True,upload_to="media/Uploads/")
    date_in=models.DateTimeField(auto_now=True)
    title=models.TextField(max_length=200)
    details=models.TextField()
    
    def __str__(self):
        return f'{self.title} is Postef by --- {self.user}'

