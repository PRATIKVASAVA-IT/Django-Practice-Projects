from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class MyuserCreationForm(UserCreationForm):
    usable_password=None
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']

class MyloginForm(AuthenticationForm):
    class Meta:
        model=User 
        fields=['username','password']       



    
  
        
