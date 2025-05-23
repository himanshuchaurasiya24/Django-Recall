from django.contrib import admin
from django.urls import path, include
from . import views as view 
urlpatterns = [
    path('students/', view.student_api), # redirects to students app urls.py file
    path('student/<int:pk>/', view.student_detail_api), # redirects to students app urls.py file
]
