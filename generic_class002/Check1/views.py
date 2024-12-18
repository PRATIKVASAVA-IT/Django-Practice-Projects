from django.shortcuts import render
from django.views.generic import CreateView
from .forms import Form_student

# Create your views here.
class studentview(CreateView):
    form_class=Form_student
    template_name='check1/index.html'
    success_url='/'