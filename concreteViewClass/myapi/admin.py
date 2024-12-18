from django.contrib import admin
from .models import student
# Register your models here.
@admin.register(student)
class StudenAdmin(admin.ModelAdmin):
    list_display=['name','city','email','roll']