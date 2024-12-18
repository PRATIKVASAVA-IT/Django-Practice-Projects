from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import SeriallizerSuperstudent
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = superstudent.objects.all()
    serializer_class =SeriallizerSuperstudent
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]



    
