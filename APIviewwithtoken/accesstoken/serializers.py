from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # Include only necessary fields

    def create(self, validated_data):
        # Ensure password is hashed
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):  
       username=serializers.CharField(max_length=100)
       class Meta:
        model = User
        fields = ['username', 'password']  # Include only necessary fields
    
     
  




         

     

