from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    


from django.contrib.auth.models import AbstractUser, Group,AbstractBaseUser
from django.db import models

class MyUser(AbstractUser):
    # Adding a custom field 'customer_id'


    customer_id = models.CharField(max_length=100,unique=True,null=True,blank=True)

    # You can also add other fields as needed

    def __str__(self):
        return self.username # Or any other field you'd prefer to represent the user
    
from django.core.validators import MinValueValidator, MaxValueValidator
   

class clinet_data(models.Model):
    
    user=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    
    weigth=models.FloatField()
    
    fate = models.FloatField(validators=[MinValueValidator(1.0),MaxValueValidator(10.0)],help_text="Please enter a value between 1 and 10.")

    types_of_milks=[('Cow','Cow'),('Buffalo','Buffalo')]

    milk_category=models.CharField(max_length=20,choices=types_of_milks,default='Buffalo',help_text='Select the type of Milk')

    price=models.FloatField()

    amount=models.FloatField()

    date=models.DateTimeField(auto_now_add=True)

    #created_by=models.CharField(max_length=20)


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    




