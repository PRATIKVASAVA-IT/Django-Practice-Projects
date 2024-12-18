from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import userModelSerializer
from .models import UserModel
from django.http import HttpRequest,HttpResponse
from rest_framework.response import Response

# Create your views here.


class Userapi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is None:
            data=UserModel.objects.all()
            stu=userModelSerializer(data,many=True)
            return Response(stu.data)
        else:
          
            user=UserModel.objects.get(id=id)
            stu=userModelSerializer(user)
            return Response(stu.data)
    def post(self,request,format=None):
        stu=userModelSerializer(data=request.data)
        if stu.is_valid():
            stu.save()
            res={'Msg':'Data Inserted Successfully!...'}
            return Response(res)    
    def put(self,request,pk,format=None):
        id=pk
        user=UserModel.objects.get(pk=id)
        stu=userModelSerializer(user,data=request.data)
        if stu.is_valid():
            stu.save()
            res={"Msg":"COMPLATE UPDATED SUCCESSFULLY..!!"}
            return Response(res)   
    def patch(self,request,pk,format=None):
        id=pk
        user=UserModel.objects.get(pk=id)
        stu=userModelSerializer(user,data=request.data,partial=True)
        if stu.is_valid():
            stu.save()
            res={"Msg":"Partially  UPDATED SUCCESSFULLY..!!"}
            return Response(res)   