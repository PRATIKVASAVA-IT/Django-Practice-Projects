from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/',views.home,name='home'),
   # path('del/<int:id>',views.#,name='del'),
    path('edit/<int:id>',views.useredit,name='edit'),
]
