from django.shortcuts import render


def index(request):
    return render(request,'layout1.html')