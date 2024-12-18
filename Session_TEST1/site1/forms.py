from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms


class User_signup_Form(UserCreationForm):
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        #fields=['username','email','password1','password2'] it will be error if using list instead of 
        fields = ['username','first_name','last_name', 'email']
        labels={'email':'Email '}

        
        


class User_login_Form(AuthenticationForm):
    class Meta:
        model=User
        fields=['Username','Password']

