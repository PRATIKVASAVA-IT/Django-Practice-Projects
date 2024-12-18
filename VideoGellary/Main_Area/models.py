from django.db import models

# Create your models here.

class author(models.Model):
    author_name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.author_name



class article_class(models.Model):
    title=models.CharField(max_length=200)
    author_name=models.ForeignKey(author, on_delete=models.CASCADE)
    desc=models.TextField()
    img=models.ImageField(default='"https://via.placeholder.com/300x200"',upload_to='Media/images/article')
    date=models.DateField()
  
    def __str__(self):
        return self.title


