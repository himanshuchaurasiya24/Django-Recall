from django.http import Http404
from .models import *
from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics,viewsets
from employee.paginations import CustomPagination



# Method 1: Using APIView class

class EmployeesListCreateAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeesRetrieveUpdateDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response({f'{employee.employee_name} has been deleted!'},status=status.HTTP_204_NO_CONTENT)
        
# Method 2: Using mixins and generics
class EmployeesListCreateMixins(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class EmployeeRetrieveUpdateDeleteMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
    
# Method 3: Using generics

class EmployeeListCreateGenerics(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDeleteGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#Method 4: Using viewsets

class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer= EmployeeSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def create(self, request):
        # queryset = Employee.objects.all() # --> Not required here...
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def retrieve(Self, request, pk=None):
        # queryset = Employee.objects.get(pk=pk)
        # serializers= EmployeeSerializer(queryset, many = True)
        employee = get_object_or_404(Employee, pk =pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def update(self, request, pk= None):
        queryset = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk = None):
        employee = get_object_or_404(Employee, pk= pk)
        employee_name = employee.employee_name
        employee.delete()
        return Response({f'{employee_name} has been deleted!'}, status=status.HTTP_204_NO_CONTENT)

# Method 5: Using ModelViewSet

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination # Custom Pagination class

