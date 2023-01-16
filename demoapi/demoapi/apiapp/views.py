
from django.shortcuts import render,HttpResponse
from apiapp.models import desc
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apiapp.serializer import dataserializer
from django.http import JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages

def index(request):
    return render(request,'Login.html')

def apidata(request):
    try:
        if request.method == 'POST':
            loginuser =request.POST.get('username')
            loginpass =request.POST.get('pass') 
            loginauth = authenticate(username=loginuser,password=loginpass)
            if loginauth is not None:
                mydata = desc.objects.all()
                mydata = list(mydata.values())
                return JsonResponse({
                    'data': mydata
                })
            else:
                messages.error(request,"Error missing field or incorret username,password")
                return render(request,'Login.html')  
        else:
            return render(request,'Login.html') 
    except:
        return render(request,'Login.html')

@api_view(['GET'])
def getdata(request):
    mydata = desc.objects.all()
    serializer = dataserializer(mydata,many = True)
    return Response(serializer.data)

# Create your views here.
@api_view(['POST','PUT','DELETE'])
def dataapi(request,id):
    mydata = desc.objects.get(pk=id)
    
    if request.method == 'POST':
        serializer = dataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'PUT':
        serializer = dataserializer(mydata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        pass

