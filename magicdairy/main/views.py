from django.shortcuts import render,redirect
from .forms import Adminlogin_form,studentForm,Adminuser_form
from .models import student
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    fm=Adminlogin_form()
    dm=studentForm()
    if request.method=='POST':
        name=request.POST.get('name')
        surname=request.POST.get('surname')
        obj=student.objects.create(name=name,surname=surname)
        messages.info(request,'Student inserted!')
        print('Student inserted Succesfully!')    
    return render (request,'main/index.html',context={"form":fm,"form1":dm})

    

from django.shortcuts import render

def regi(request):
    if request.method == 'POST':
        fm = Adminuser_form(request.POST)
        
        if fm.is_valid():
            user = fm.save(commit=False)  # Create the user object but don't save to the database yet
            user.is_staff = True         # Set staff_status to True
            user.save()     
            group=Group.objects.get(name='writer')
            user.groups.add(group)
            

            messages.info(request,'User successfully created !')
            # Success! Redirect or show a confirmation message
            return redirect('/regi/')  # Redirect to success page
        else:
            return render(request, 'main/registration.html', context={'fm': fm})
    else:
        fm = Adminuser_form()
        return render(request, 'main/registration.html', context={'fm': fm})