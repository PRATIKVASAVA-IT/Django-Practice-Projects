from rest_framework import serializers
from django.contrib.auth.models import User
   
class RegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']
        