
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import settings
from django.conf.urls.static import static

from MyProject2.settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App1.urls')),
]+static(settings.Media_URL,document_Root=settings.Media_Root)
