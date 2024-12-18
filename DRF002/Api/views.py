from urllib import request
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import studentserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import * 

# Create your views here.


def get_data(request):

    if request.method=="GET":
        query=student.objects.all()
        serializer3=studentserializer(query,many=True)
        json_data=JSONRenderer().render(serializer3.data)
        return HttpResponse(json_data,content_type='application/Json')
    
@csrf_exempt
def update_data(request):
    
    if request.method=='PUT':
        jdata=request.body
        stream=io.BytesIO(jdata)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=student.objects.get(id=id)
        s4=studentserializer(stu,data=pydata,partial=True)
        if s4.is_valid():
            s4.save()
            res='Updated your data'
            jason_data=JSONRenderer().render(res)
            return HttpResponse(jason_data,content_type='application/Json')
        jason_data=JSONRenderer().render(s4.errors)
        return HttpResponse(jason_data,content_type='application/Json')
        
        





@csrf_exempt
def set_data(request):

    if request.method=="POST":
        json_data=request.body

        strea=io.BytesIO(json_data)
        pydata=JSONParser().parse(strea)
        serializer2=studentserializer(data=pydata)
        if serializer2.is_valid():
            serializer2.save()
            res='Data Inserted Successfully'
            contexdata=JSONRenderer().render(res)
            return HttpResponse(contexdata,content_type='application/Json')
        contexdata=JSONRenderer.render(serializer2.errors)
        return HttpResponse(contexdata,content_type='application/Json')
    
    



