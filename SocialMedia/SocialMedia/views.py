from django.shortcuts import redirect,render
from django.contrib.auth import login,logout
from my_post.models import user_post,User


def index(request):
    return render(request,'register.html')


