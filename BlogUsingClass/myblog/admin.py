from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class Admin_blog(admin.ModelAdmin):
    list_display=['user','title','description','img','date']