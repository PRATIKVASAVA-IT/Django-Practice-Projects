from django import forms
from django.contrib.auth.models import User
from .models import Myclass
class userform(forms.ModelForm):
    
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','first_name','last_name','password']
        widgets={'password':forms.PasswordInput()}

        
