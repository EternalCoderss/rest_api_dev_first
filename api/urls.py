from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')
router.register('departments', views.DepartmentViewSet, basename='department')
"""
if using EmployeeViewSet we need to add basename as well
"""


urlpatterns = [
     # normal url --

    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),

    # employee urls ---

    # path('employees/', views.Employees.as_view()),
    # path('employees/<pk>/', views.EmployeesDetail.as_view()),

    #router based ---

     path('', include(router.urls)),
     path('departments/', include(router.urls)),

]