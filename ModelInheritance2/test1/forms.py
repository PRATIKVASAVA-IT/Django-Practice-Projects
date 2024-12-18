from django import forms
from .models import customer,Address

class cutomercreatinForm(forms.ModelForm):
     
    class Meta:
        model=customer
        fields=['cust_name','cust_surname','add1','add2','add3','city','state','country','pin']
        
        
        