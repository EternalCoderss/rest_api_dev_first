from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
# Create your views here.
from students.models import Student
from employees.models import Employee


from .serializers import StudentSerializer , EmployeeSerializer
from  rest_framework.response import Response
from rest_framework import status

#if i want to only the data show in get request then we will use decorator -  like APIView

from rest_framework.decorators import api_view

# class based --

from rest_framework.views import APIView 
from django.http import Http404
# class end
#class - mixin -- 
from rest_framework import mixins, generics , viewsets

@api_view(['GET', 'POST'])
def studentView(request):
    
    # students = list(Student.objects.values())
    # print(students)
    # # serializer = 
    
    # return JsonResponse(students, safe=False)

    if request.method == "GET":
        students  = Student.objects.all()
        serializer = StudentSerializer(students, many = True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try: 
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        #yaha prepopulate kr rahe data isliye student aaya -  and ata = request.data

        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




    # Class Based Views ---

# class Employees(APIView):

#     def get(self, request):
#         employees  = Employee.objects.all()
#         print(employees)

#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class EmployeesDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):

#         employee  = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Class Based Mixin - list and create mixins

"""
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

class EmployeesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset  = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
    """
# ListCreateAPIView --
# Generics --


class Employees(generics.ListAPIView, generics.CreateAPIView):
    """
    # listCreateAPIView - 
    # can take care of both at once listing and Creating.

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesDetail(generics.RetrieveAPIView, generics.UpdateAPIView , generics.DestroyAPIView): 
    """
     DestroyAPIView
     RetrieveUpdateAPIView ,
     RetrieveUpdateDestroyAPIView , 
     RetrieveDestroyAPIView -
     
     also can be used to make all task using one APIView

     its a pk based operation coz we want to fetch data based on pk from the DB.

    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

    """
    ViewSets - ( Set of views - it combines the functionalities of both views and serializers, 
    we dont have to need write seprate classes for listview or detailview etc)

    two method - 
    
    viewsets.ViewSet -- list, create, retrive , update , delete 

    viewsets.ModelViewSet  -- it just takes queryset and serializer_class and automatically provides both pk based or non-pk based operations.

    using viewset we need to use Routers , we can't just explicitly use the urlpatterns 

    """

class EmployeeViewSet(viewsets.ViewSet):

    def list(self , request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many = True)
        return Response(serializer.data)
    

    def create( self, request):
        serializer = EmployeeSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data= request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)


    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)