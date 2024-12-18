from django.shortcuts import render
from  django.views.generic.edit import CreateView
from  django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .forms import MyuserCreationForm,MyloginForm
from django.contrib import messages
from rest_framework.generics import ListCreateAPIView
from .serializers import RegisterSerilizer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class RegistrationView(CreateView):
    model=User
    form_class=MyuserCreationForm
    success_url='/'
    template_name='testApi/registration.html'


    def form_valid(self, form):
        # Save the form and pass a success message
        response = super().form_valid(form)
        messages.success(self.request, 'Registration successful!')
        return response
    
class loginview(CreateView):
    model=User
    form_class=MyloginForm
    success_url='/'
   
    template_name='testApi/userlogin.html'    

class dashboardview(TemplateView):
    template_name='testApi/dashboard.html'    


class apiregisterview(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=RegisterSerilizer
    #authentication_classes=[SessionAuthentication]
    #permission_classes=[IsAuthenticated]



    
