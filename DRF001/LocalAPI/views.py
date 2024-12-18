from django.shortcuts import render
from .models import EnrollStudent
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import EnrollStudentSerializer
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


# query set - for all data
def RequestProcessor(request):
    # FETCING ALL DATA FROM db
    q1=EnrollStudent.objects.all()
    #converting complex data into python data type
    pdata=EnrollStudentSerializer(q1,many=True)
    #convdeting pyton data into json for rendering
    jdata=JSONRenderer().render(pdata.data)
    return HttpResponse(jdata,content_type='application/Json')

# For a Model Instance only


def RequestProcessorStandAlone(request,pk):
    # single instance query
    q2=EnrollStudent.objects.get(id=pk)
    # convert model instance into python data
    p1=EnrollStudentSerializer(q2)
    #convert python obj into Json
    j1=JSONRenderer().render(p1.data)
    # rendering response to the Html page
    return HttpResponse(j1,content_type='application/Json')

@csrf_exempt
def createProcess(request):
    if request.method=='POST':
        j_data=request.body
        stream=io.BytesIO(j_data)
        pythondata=JSONParser().parse(stream)
        serializer=EnrollStudentSerializer(pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Inserted!'}
            data=JSONRenderer().render(res)
            return HttpResponse(data,content_type='application/Json')
        return HttpResponse(serializer.errors)

            

    
    
    


    