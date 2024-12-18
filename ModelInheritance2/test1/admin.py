from django.contrib import admin
from .models  import Address,customer

# Register your models here.
@admin.register(Address)
class addressAdmin(admin.ModelAdmin):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display = [field.name for field in self.model._meta.fields]


@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display = [field.name for field in self.model._meta.fields]
        

    