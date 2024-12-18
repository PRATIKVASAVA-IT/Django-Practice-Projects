from django.contrib import admin
from django import forms
from .models import student
# Register your models here.
@admin.register(student)
class Admin_student(admin.ModelAdmin):
    list_display=['name','password']