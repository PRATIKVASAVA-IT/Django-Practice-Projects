from django.shortcuts import render
from .forms import cutomercreatinForm
from .models import customer
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
         fm=cutomercreatinForm(request.POST)
         if fm.is_valid():
              messages.success(request,'Successfully Customer Added ')
              fm.save()
              
              fm=cutomercreatinForm()
              return render(request,'test1/index.html',{'fm':fm})    
         else:
            return render(request,'test1/index.html',{'fm':fm})     

    else:
         fm=cutomercreatinForm()
    return render(request,'test1/index.html',{'fm':fm})