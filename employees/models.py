from django.db import models
import uuid

# Create your models here.


class BaseMixin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Department(BaseMixin):
    dept_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.dept_name

    
class Employee(BaseMixin):
    emp_name = models.CharField(max_length=100)
    emp_salary = models.DecimalField(decimal_places=2, max_digits=10)
    designation = models.CharField(max_length=50)

    department = models.ForeignKey(Department, null=True, blank=True,  related_name='employees', on_delete=models.CASCADE)

    """
    The related_name="employees" lets you access all employees in a department via department.employees.all().
    """

    def __str__(self):
        return self.emp_name