from django.shortcuts import render
from .forms import customer_form1
from .models import customer,Address
from django.contrib import messages

# Create your views here.
def index (request):
    if request.method=='POST':
        fm=customer_form1(request.POST)
        if fm.is_valid():
            fm.save()
        return render(request,'index.html')  
    else:
        fm=customer_form1()
        add=Address.objects.all()
    return render (request,'index.html',{'fm':fm,'add':add})   
 
         
    
    
    
    
