from django.urls import include, path
from .models import *
from .views import *
from . import views
# for viewsets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# Method 4: Using ViewSets
# router.register('employees',views.EmployeeViewSet,basename='Employee ViewSet')

# Method 5: Using ModelViewSet
router.register('employees',views.EmployeeModelViewSet,basename='Employee ModelViewSet')




urlpatterns = [
    # Method 1: Using APIView class
    # path('', EmployeesListCreateAPIView.as_view(), name='employee-list-create'),
    # path('details/<int:pk>/', EmployeesRetrieveUpdateDeleteAPIView.as_view(), name='employee-retrieve-update-delete'),

    # Method 2: Using mixins and generics
    # path('', EmployeeListCreateMixins.as_view(), name='employee-list-create'),
    # path('details/<int:pk>/', EmployeeRetrieveUpdateDeleteMixins.as_view(), name='employee-retrieve-update-delete'),

    # Method 3: Using generics
    # path('', EmployeeListCreateGenerics.as_view(), name='employee-list-create'),
    # path('details/<int:pk>/', EmployeeRetrieveUpdateDeleteGenerics.as_view(), name='employee-retrieve-update-delete'),

    # Method 4: Using viewsets
    # path('', include(router.urls), ),

    # Method 5: Using ModelViewSet
    path('', include(router.urls), )
]

