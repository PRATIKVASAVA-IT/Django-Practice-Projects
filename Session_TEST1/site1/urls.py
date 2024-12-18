from django.contrib import admin
from django.urls import path,include
from site1 import views
urlpatterns = [
path('',views.index,name='home'),
path('signup/',views.signup,name='signup'),
path('profile/',views.profile,name='profile'),
path('login/',views.user_login,name='login'),
path('logout/',views.user_logout,name='logout'),
 
]