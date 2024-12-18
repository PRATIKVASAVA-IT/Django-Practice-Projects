from django.contrib import admin
from .models import Address,customer,Profile
# Register your models here.

@admin.register(Address)
class Address_app(admin.ModelAdmin):
    list_display=['add1','add2','city','dis','state','country']
@admin.register(customer)
class customer_app(admin.ModelAdmin):
    list_display=['add1','add2','city','dis','state','country','name','mobile','email']

@admin.register(Profile)
class profile_app(admin.ModelAdmin):
    list_display=['add1','add2','city','dis','state','country','name','mobile','email','date']









