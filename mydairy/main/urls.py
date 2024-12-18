from django.contrib import admin
from django.urls import path,include
from main import views

urlpatterns = [
    
path('',views.index,name='index'),
path('con/',views.control_page,name='con'),
path('regi/',views.regi,name='regi'),
path('a_login/',views.admin_login,name='admin_login'),
path('a_logout/',views.admin_logout,name='admin_logout'),
path('clda',views.clientData,name='cd'),




]