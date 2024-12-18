from django.shortcuts import render,HttpResponse
from .forms import Xyz1
from .models import UserAdd

# Create your views here.\
def home(request):
        db_data=UserAdd.objects.all()
        if request.method=='POST':
            


        
        
            fm=Xyz1(request.POST)
            if fm.is_valid():
                  nm=fm.cleaned_data['name']
                  em=fm.cleaned_data['email']
                  mb=fm.cleaned_data['mobile']
                  pw=fm.cleaned_data['password']
                  si=UserAdd(name=nm,email=em,mobile=mb,password=pw)
                  si.save()
                  fm=Xyz1()  
                  return render(request,'main/home.html',{'form1':fm,'msg':'User Added successfully','data': db_data})
                

        else:
            db_data=UserAdd.objects.all()
            fm=Xyz1()  
            
            return render(request,'main/home.html',{'form1':fm,'data': db_data})

          


def useredit(request,id):
      if request.method=='POST':
            in1=UserAdd.objects.get(id=id)
            fm=Xyz1(instance=in1)
            return render(request,'main/user_edit.html',{'form1':fm})