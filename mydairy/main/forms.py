from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import clinet_data,MyUser
from django.contrib.auth.models import Group


class myuser_form(UserCreationForm):
    usable_password=None
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Change widget as needed
        required=False,
        label="Assign Groups")
    
    class Meta:
        model =MyUser
        fields = ['username','first_name','last_name','email','groups']         


class admin_login_form(AuthenticationForm):
    class Meta:
        model=MyUser
    username = forms.CharField(
        label="Username",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-control'})
    )
       
        

  
class client_data_form(forms.ModelForm): 
    class Meta:
        model=clinet_data
        fields=['weigth','fate','milk_category','price','amount']
