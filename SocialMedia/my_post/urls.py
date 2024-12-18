from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .forms import *


urlpatterns = [
        path('',All_post,name="post"),
        path('Create_post/',Create_post,name='Create_post'),
        path('edit_post/<int:id>/',edit_post,name='edit_post'),
        path('delete_post/<int:id>/', delete_post, name='delete_post'),
        path('register/',register,name='register'),
        path('search/',search,name='search'),
        

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
