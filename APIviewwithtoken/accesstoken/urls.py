from django.contrib import admin
from django.urls import path,include
from accesstoken import views

urlpatterns = [
   path('register/',views.Apiregisterview.as_view(),name='Apiregister'),
   path('login/',views.Apiloginview.as_view(),name='Apilogin')
]
