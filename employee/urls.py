from django.urls import include, path
from .models import *
from .views import *

urlpatterns = [
    # Method 1: Using APIView class
    # path('', EmployeesListCreateAPIView.as_view(), name='employee-list-create'),
    # path('details/<int:pk>/', EmployeesRetrieveUpdateDeleteAPIView.as_view(), name='employee-retrieve-update-delete'),

    # Method 2: Using mixins and generics
    # path('', EmployeeListCreateMixins.as_view(), name='employee-list-create'),
    # path('details/<int:pk>/', EmployeeRetrieveUpdateDeleteMixins.as_view(), name='employee-retrieve-update-delete'),

    # Method 3: Using generics
    path('', EmployeeListCreateGenerics.as_view(), name='employee-list-create'),
    path('details/<int:pk>/', EmployeeRetrieveUpdateDeleteGenerics.as_view(), name='employee-retrieve-update-delete'),
]

