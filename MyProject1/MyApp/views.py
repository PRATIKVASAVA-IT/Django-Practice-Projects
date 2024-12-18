from django.shortcuts import render
from django import urls

# Create your views here.

def index(request):
    return render(request,'index.html')
