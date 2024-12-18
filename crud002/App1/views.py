from django.shortcuts import render,HttpResponse
from .forms import userform
from django import forms
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    data=User.objects.all()
    if request.method=='GET':
        if data:
            fm=userform()
            return render(request,'home.html',{'form1':fm,'data':data})
        else:
            
            fm=userform()
            return render(request,'home.html',{'form1':fm,'data':'No Record Found'})
        
        
    if request.method=='POST':
        fm=userform(request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['username']
            fn=fm.cleaned_data['first_name']
            ln=fm.cleaned_data['last_name']
            pw=fm.cleaned_data['password']
            dt=User(username=un,first_name=fn,last_name=ln,password=pw)
            dt.save()
            fm=userform()
            

        return render(request,'home.html',{'form1':fm,'data':data})
    

 
        
       
