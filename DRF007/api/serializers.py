from rest_framework import serializers
from .models import superstudent

class SeriallizerSuperstudent(serializers.ModelSerializer):
    class Meta:
        model=superstudent
        fields=['name','roll','city']