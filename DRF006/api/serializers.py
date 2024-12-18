from rest_framework import serializers
from .models import * 

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=users
        fields=['id','name','roll','city']

