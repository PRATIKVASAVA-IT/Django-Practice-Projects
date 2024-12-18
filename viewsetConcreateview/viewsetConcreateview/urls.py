"""
URL configuration for viewsetConcreateview project.

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
from django.urls import path,include
from myapi import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()
router.register('studentapi',views.studentview,basename='student')
#router.register('studentapi/',views.studentRUDview,basename='student2')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',TokenObtainPairView.as_view(),name='TokenObtainPairView'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='TokenRefreshview'),
    path('verifytoken/',TokenVerifyView.as_view(),name='TokenObtainPairView'),
 
]
