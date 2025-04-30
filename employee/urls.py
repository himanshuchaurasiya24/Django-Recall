from django.urls import include, path
from .models import *
from .views import *

urlpatterns = [
    path('', EmployeesListCreate.as_view(), name='employee-list-create'),
    path('employee/<int:pk>/', EmployeesRetrieveUpdateDelete.as_view(), name='employee-retrieve-update-delete'),
    # path('employees/', EmployeeListCreate.as_view(), name='employee-list-create'),
    # path('employee/<int:pk>/', EmployeeRetrieveUpdateDelete.as_view(), name='employee-retrieve-update-delete'),
]

