from django.contrib import admin
from django.urls import path, include
from . import views as view
urlpatterns = [
    path('', view.students),
]