from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def student_api(request):
    #37.04
    students = {
        'id': 1, 'name': 'John Doe', 'age': 20, 'major': 'Computer Science'
    }
    return JsonResponse(students)
