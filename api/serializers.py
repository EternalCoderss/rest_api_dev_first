from rest_framework import serializers
from students.models import Student
from employees.models import Employee, Department


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

# Department Serializer -

class DepartmentSerializer(serializers.ModelSerializer):
    """
    If i want the nested data - from the employee serializer
    related name. = serializername of that model,
    That one single line will bring all employee in that department -- many = true will help if employe are multiple.

    """
    class Meta:
        model = Department
        fields = '__all__'

# Employee Serializer -

class EmployeeSerializer(serializers.ModelSerializer):
    """
     NOTE: Agar nested data laana serializer me to ye top to bottom approach hi follow krega. 
            Also Department ForiegnKey hai employee model me, agar department me employee ka ese Nested serializer field bnate h.
    """
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'  