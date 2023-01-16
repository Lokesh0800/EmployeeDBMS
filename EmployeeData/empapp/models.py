from django.db import models

# Create your models here.
class Department(models.Model): 
    Department_name = models.CharField(max_length=50,null=True)
    Status = models.CharField(max_length=10,null=True)
    
    def __str__(self):
        return self.Department_name

class Employees(models.Model):
    Empname = models.CharField(max_length=20,null=True)
    Designation = models.CharField(max_length=20,null=True)
    Department = models.CharField(max_length=20,null=True)
    DOJ = models.DateField(null=True)
    Contact = models.CharField(max_length=10,null=True)
    CTC = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.Empname
    
    

