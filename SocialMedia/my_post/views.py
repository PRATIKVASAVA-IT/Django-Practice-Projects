from django.shortcuts import render,redirect,get_list_or_404
from .models import user_post,User
from my_post.forms import post_form,UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

# Create your views here.
def All_post(request):
    AP=user_post.objects.all().order_by('-id')
    return render(request,'post.html',{'poster':AP})

@login_required
def Create_post(request):
    
    if request.method=='POST':
        f1=post_form(request.POST,request.FILES)
        if f1.is_valid():
            post=f1.save(commit=False)
            post.user=request.user
            post.save()
    
            return redirect('post')
            
            
        else:
            return 'Somthing went wrong!'    
    
    else:
        f1=post_form()
        return render(request,'Create_post.html',{'form':f1})
    

            

@login_required
def edit_post(request,id):
    tp=user_post.objects.get(id=id)
    if request.method=='POST':
        post=post_form(request.POST,request.FILES,instance=tp)
        if post.is_valid():
            post.save()
            return redirect('post')
    else:
        f1=post_form(instance=tp)
    return render(request,'edit_post.html',{'form':f1})

@login_required
def delete_post(request,id):
    tp=user_post.objects.get(id=id)
    tp.delete()
    return redirect('post')
    


def register(request):
    if request.method=="POST":
        form1=UserRegistrationForm(request.POST)
        if form1.is_valid():
            post=form1.save(commit=False)
            post.set_password(form1.cleaned_data['password1'])
            post.save()
            login(request,User)
        return redirect('post')
    else:
        form=UserRegistrationForm()
        return render (request,'registration/register.html',{'form':form})
    
    
def search(request):
    if request.method=='GET':
        n1=request.GET.get('search')
        query=user_post.objects.filter(title__icontains=n1)
        return render(request,'search_post.html',{'query':query})
            
        


