from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from .models import student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class studentview(ViewSet,ModelViewSet):
    queryset=student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]
    
