from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserAdd


class Xyz1(forms.ModelForm):
    class Meta:
        model=UserAdd
        fields=['name','email','mobile','password']
       # fields='__all__'
  
       





