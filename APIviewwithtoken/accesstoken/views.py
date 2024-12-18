from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
class Apiregisterview(APIView):
    def post (self,request,format=None):
        sz=RegisterSerializer(data=request.data)
        if sz.is_valid():
            user=sz.save()
            token=get_tokens_for_user(user)
            return Response({"token":token,"Event":" ...Registration Successfully!"})
        else:
            return Response({"error":sz.errors}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

class Apiloginview(APIView):
    def post(self,request,format=None):
        sz=LoginSerializer(data=request.data)
        if sz.is_valid():
            un=sz.data.get('username')
            pw=sz.data.get('password')
            uz=authenticate(username=un,password=pw)
            if uz is not None:
                token=get_tokens_for_user(uz)
                #return HttpResponse('pk')
                return Response({"token":token,"Msg":"Login Successfully!"})
            return Response({"msg":"Likewise "})
        else:
            return Response(sz.errors)

class ApiProfileview(APIView):
    def post(self,request,format=None):
        permission_class=[IsAuthenticated]