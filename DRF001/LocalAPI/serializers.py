from .models import *
from rest_framework import serializers

class EnrollStudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=100)
    rn=serializers.IntegerField()

    def create(self,validated_data):
        return EnrollStudent.objects.create(**validated_data)

