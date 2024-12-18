from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import User_login_Form,User_signup_Form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    return render (request,'site1/check1.html',{'title':'Home'})

def signup(request):
    if request.method=='POST':
        fm=User_signup_Form(request.POST)
        if fm.is_valid():
            messages.success(request,'User Created Successfully')
            fm.save()
            fm=User_signup_Form()
            return render(request,'site1/check1.html',{'fm':fm,'title':'SignUp'})
        else:
             return render(request,'site1/check1.html',{'fm':fm,'title':'SignUp'})  
    else:
        fm=User_signup_Form()
    #return render(request,'site1/CreateUSer.html',{'form':fm})
    return render(request,'site1/check1.html',{'fm':fm,'title':'SignUp'})    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None: 
                    login(request,user)
                    messages.success(request,f'LOGIN Successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:  
            fm=AuthenticationForm()
        return render(request,'site1/loginUser.html',{'fm':fm})     
    else:
         messages.success(request,f'your Login Time is for ')
         return HttpResponseRedirect('/profile/')
         
        

def profile(request):
    return  render (request,'site1/profile.html')    


def user_logout(request):
    logout(request)
    messages.success(request,'LOGOUT Successfully')
    return HttpResponseRedirect('/login/')
