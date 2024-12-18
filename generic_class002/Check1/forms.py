from django import forms
from .models import student

class Form_student(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','password']