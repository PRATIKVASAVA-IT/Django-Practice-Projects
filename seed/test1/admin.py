from django.contrib import admin
from .models import student


# Register your models here
@admin.register(student)
class Adminstu(admin.ModelAdmin): # type: ignore
    list_display=['name','address','email','age']


