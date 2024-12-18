from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class post_form(forms.ModelForm):
    class Meta:
        model=user_post
        fields = ['title', 'details', 'photo']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')