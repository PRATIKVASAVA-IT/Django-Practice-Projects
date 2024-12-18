from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import users
from .serializers import userserializer
# Create your views here.


@api_view(['GET','POST'])
def apiresult(request):
    if request.method=='GET':
        user=users.objects.all()
        all_data=userserializer(user,many=True)
        return Response(all_data.data)
    
    
    if request.method=='POST':
        user1=userserializer(data=request.data)
        if user1.is_valid():
            user1.save()
            return Response({"Msg":"Record Successfully Saved !"})
        return Response(user1.errors)

    