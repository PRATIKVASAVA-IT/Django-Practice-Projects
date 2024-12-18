from django import forms
from .models import Login_customer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class Form_Login_Customer(forms.ModelForm):
     class Meta:
        model = Login_customer
        fields ='__all__'
  
        

    
