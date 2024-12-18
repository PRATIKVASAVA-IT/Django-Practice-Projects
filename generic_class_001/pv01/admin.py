
from django.contrib import admin
from .models import Login_customer

@admin.register(Login_customer)
class Admin_Login_customer(admin.ModelAdmin):
    list_display = ['uname', 'password']  # Ensure these fields are correct
