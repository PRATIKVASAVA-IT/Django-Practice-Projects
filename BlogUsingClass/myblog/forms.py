from django import forms

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Blog

class user_registrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class blog_form(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
    

    
                  
