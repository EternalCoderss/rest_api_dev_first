from django.urls import path
from . import views


urlpatterns = [

    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),

    # employee urls 

    path('employees/', views.Employees.as_view()),
    path('employees/<pk>/', views.EmployeesDetail.as_view()),


]