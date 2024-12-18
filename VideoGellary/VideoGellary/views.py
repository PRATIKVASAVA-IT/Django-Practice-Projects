from django.http import HttpResponse,request
from django.shortcuts import render,redirect
from Main_Area.models import *
from .forms import *


def index(request):
    query=article_class.objects.all()
    return render(request,'VG/index.html',context={"data":query})


def check(request):
    f1=check_form()
    return render(request,'VG/check001.html',{'form1':f1})
    
def reciverCheck001(request):
  if request.method == 'GET':
     f1=request.GET.get('name')
     
     return render(request,'VG/reciverCheck001.html',{'data':f1})
  
 