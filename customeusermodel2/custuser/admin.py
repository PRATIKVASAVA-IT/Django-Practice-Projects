from django.contrib import admin
from custuser.models import mycustomeuser,trackermodel
# Register your models here.

# method 1
class mycutomeuserAdmin(admin.ModelAdmin):
    list_display=('mobile','date_joined','last_login')


admin.site.register(mycustomeuser,mycutomeuserAdmin)

# Metod 2
@admin.register(trackermodel)
class trackemodelAdmin(admin.ModelAdmin):
    list_display=('comment','amount','user')
