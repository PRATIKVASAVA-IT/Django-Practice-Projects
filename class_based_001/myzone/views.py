from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.base import TemplateView,RedirectView
from .forms import FormCustomer
# Create your views here.
class cutomerAdditionView(CreateView):
    form_class=FormCustomer
    field=['username','first_name','last_name','password']
    success_url='/profile/'
    template_name='myzone/Regi.html'

class profileview(TemplateView):
    template_name='myzone/profile.html'

class Homeview(TemplateView):
    template_name='myzone/index.html'
