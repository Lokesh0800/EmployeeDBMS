from django import forms
from django.forms import ModelForm
from .models import Employees,Department

class empform(ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
        labels = {
            'Empname':'',
            'Designation':'',
            'Department':'',
            'DOJ':'',
            'Salary':'',
            'Contact':'',
        }
        
        widgets={
            'Empname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}),
            'Designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Position'}),
            'Department':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}),
            'DOJ':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter DOJ','type':'date'}),
            'Salary':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter salary'}),
            'Contact':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact'}),
        }

class departmentform(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        labels = {
            'Department_name':'',
            'Status':'',
        }
        
        widgets = {
            "Department_name": forms.TextInput(attrs={'class':'form-control'}),
            "Status": forms.TextInput(attrs={'class':'form-control'}),
        }