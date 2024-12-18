"""
URL configuration for BlogUsingClass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.BlogListView.as_view(),name='home'),
    path('login/',auth_view.LoginView.as_view(template_name='myblog/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='myblog/logout.html'),name='logout'),
   
    path('registration/',views.UserRegistrationCreateView.as_view(),name='registration'),
    path('success/',views.successView.as_view(),name='success'),
    path('dashboard/',views.dashboardView.as_view(),name='dashboard'),
    path('blog/',views.BlogView.as_view(),name='blog'),
    path('postview/<int:pk>/',views.PostDetailView.as_view(),name='PostView'),
    path('Updateblogview/<int:pk>/',views.UpdateBlogView.as_view(),name='updateView'),
    path('SearchListView/',views.SearchListView.as_view(),name='Searchview'),
    path('DeleteView/<int:pk>/',views.myDeleteview.as_view(),name='DeleteView'),
    path('apidata/',views.apidata,name='apidata')
    
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
