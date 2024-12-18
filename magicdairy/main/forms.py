from django.forms import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import student
from django import forms

class Adminlogin_form(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username','password']

class studentForm(forms.ModelForm):  # Use ModelForm instead of Form
    class Meta:
        model =student  # Reference the correct model
        fields = '__all__'  # Correct the typo

class Adminuser_form(UserCreationForm):


    class Meta:
        model= User
        fields=['username','first_name','last_name','email']


    

