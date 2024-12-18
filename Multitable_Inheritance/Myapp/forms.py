from .models import Address,customer,Profile
from django import forms


 
class customer_form1(forms.ModelForm):
    class Meta:
        model=customer
        fields='__all__'