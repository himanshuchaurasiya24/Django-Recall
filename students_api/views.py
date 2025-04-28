from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from students_api.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# 01:22:42
@api_view(['GET', 'POST'])
def student_api(request):
    students = Student.objects.all()
    # manual serialization of queryset
    # students_list =list(students.values())

    # serializer of drf that converts queryset to json
    # Function based views 
    if request.method == 'GET':
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data, 
                        status=status.HTTP_200_OK
                        )
    elif request.method == 'POST':
        serializers = StudentSerializer(data= request.data)
        if serializers.is_valid():
            serializers.save() # data is stored in database
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        print(serializers.errors)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # return JsonResponse(students_list, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_api(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'No student found for this id'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data) # student is the instance to be updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = StudentSerializer(student)
        student.delete()
        return Response(serializer.data, status= status.HTTP_204_NO_CONTENT)
        
            
        
    
        
