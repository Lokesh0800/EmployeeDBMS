from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    Emp_id = models.IntegerField(primary_key=True)
    Emp_name = models.CharField(max_length=20,null=True)
    designation = models.CharField(max_length=20,null=True)
    department = models.CharField(max_length=20,null=True)
    doj = models.DateField(null=True)
    contact = models.IntegerField(null=True)
    
    def __str__(self):
        return self.Emp_name