from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import mycustomeuser,trackermodel


class registration_form_user(UserCreationForm):
    # to hide password_authentication options
    usable_password=None


    class Meta:
        model=mycustomeuser
        fields=['mobile','first_name','last_name','email','profile_photo']


class trackerform(forms.ModelForm):
    
    class Meta:
        model=trackermodel
        fields=['comment','amount']

    
   