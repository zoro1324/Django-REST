# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializers
from .models import Person

# Create your views here.

@api_view(['GET','PUT'])
def index(request):

    student_data = {
        'name' : 'Ramu',
        'friends'  : ['Somu','Babu'],
    }
    if request.method == 'PUT':
        data = request.data
        print(data)
    elif request.method == 'GET':
        print('----------------------------')
        print(request.GET.get('search'))
        print('----------------------------')
    return Response(student_data)

@api_view(['POST','GET','PATCH','PUT','DELETE'])
def person(request):

    if request.method == 'POST':
        data = request.data
        serializer = PersonSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'GET':
        obj = Person.objects.all()
        serializer = PersonSerializers(obj,many=True)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        data = request.data
        
        obj = Person.objects.get(id=data['id'])
        serializer = PersonSerializers(obj,data=data,partial = True)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'PUT' :
        data = request.data
        serializer = PersonSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == "DELETE":
        data = request.data 
        try:
            obj = Person.objects.get(id=data['id'])
            obj.delete()
            return Response({"message":"Deleted"})
        except Person.DoesNotExist:
            return Response({"message":"Invalid"})
        
