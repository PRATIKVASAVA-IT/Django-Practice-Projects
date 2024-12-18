from django.contrib.auth.models import BaseUserManager

class usermanager(BaseUserManager):
    def create_user(self,mobile,password=None,**extra_fields):
        if not mobile:
            raise ValueError()
        user=self.model(mobile=mobile,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,mobile,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('STAFF FILED IS REQUIRED')
        
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser FILED IS REQUIRED')
        
        
        if extra_fields.get('is_active') is not True:
            raise ValueError('active FILED IS REQUIRED')
        
        return self.create_user(mobile,password,**extra_fields)