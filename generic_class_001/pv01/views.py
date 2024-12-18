from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView,CreateView

from .models import Login_customer
from .forms import Form_Login_Customer

# Create your views here.
class CusotmerLoginView(CreateView):
    form_class=Form_Login_Customer
    template_name='pv01/cust_login.html'
    success_url='/'



    
