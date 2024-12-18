from django.shortcuts import render
from requests import request
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


# Class Based View 

@method_decorator(csrf_exempt,name='dispatch')
class studentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id',None)
        if id is not None:
            stu=student.objects.get(id=id)
            s1=studentserializer(stu)
            #res="INSTANCE IS FATCHED"
            return JsonResponse(s1.data,safe=False)
        
            
        stu=student.objects.all()
        s1=studentserializer(stu,many=True)   
        #res="Data Record  IS FATCHED"
        return JsonResponse(s1.data,safe=False)

    def post(self,request,*args,**kwargs):
        
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        s1=studentserializer(data=pydata)
        if s1.is_valid():
            s1.save()
            res='Record saved Successfully'
            return JsonResponse(res,safe=False)
        return JsonResponse(s1.errors,safe=False)
        
    def put(self,request,*args,**kwargs):
        
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        if(len(pydata)==len(student._meta.fields)): # comapre the filed between requested query and exisitng db fields
            # if match --> fully update Done
            stu=student.objects.get(id=id) 
            s1=studentserializer(stu,data=pydata)
            if s1.is_valid():
                s1.save()
                res='Full Updated Successsfully'
                return JsonResponse(res,safe=False)
            return JsonResponse(s1.errors,safe=False)
        
         # else --> partialy update 
        stu1=student.objects.get(id=id)
        s2=studentserializer(stu1,data=pydata,partial=True)
        if s2.is_valid():
            s2.save()
            res='Partially Updated Successsfully'
            return JsonResponse(res,safe=False)
        return JsonResponse(s1.errors,safe=False)
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        res='Record is Deleted Successfully'
        return JsonResponse(res,safe=False)
    


    





# Function Based View

'''
@csrf_exempt
def SearchAPI(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id',None)
        if id is not None:
            stu=student.objects.get(id=id)
            s1=studentserializer(stu)
            #res="INSTANCE IS FATCHED"
            return JsonResponse(s1.data,safe=False)

            
        stu=student.objects.all()
        s1=studentserializer(stu,many=True)   
        #res="Data Record  IS FATCHED"
        return JsonResponse(s1.data,safe=False)

    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        s1=studentserializer(data=pydata)
        if s1.is_valid():
            s1.save()
            res='Record saved Successfully'
            return JsonResponse(res,safe=False)
        return JsonResponse(s1.errors,safe=False)
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        if(len(pydata)==len(student._meta.fields)): # comapre the filed between requested query and exisitng db fields
            # if match --> fully update Done
            stu=student.objects.get(id=id) 
            s1=studentserializer(stu,data=pydata)
            if s1.is_valid():
                s1.save()
                res='Full Updated Successsfully'
                return JsonResponse(res,safe=False)
            return JsonResponse(s1.errors,safe=False)
        
         # else --> partialy update 
        stu1=student.objects.get(id=id)
        s2=studentserializer(stu1,data=pydata,partial=True)
        if s2.is_valid():
            s2.save()
            res='Partially Updated Successsfully'
            return JsonResponse(res,safe=False)
        return JsonResponse(s1.errors,safe=False)
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        res='Record is Deleted Successfully'
        return JsonResponse(res,safe=False)
        
'''