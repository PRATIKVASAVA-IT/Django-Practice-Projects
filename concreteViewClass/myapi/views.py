from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import student
from .serializers import StudentSerializer
# Create your views here.


class StudentApiview(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializer

class StudentApiRUD(RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()  
    serializer_class=StudentSerializer  
