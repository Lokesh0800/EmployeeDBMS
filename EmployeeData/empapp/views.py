from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import empform,departmentform

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('adminpage')
        else:
            msg = messages.error(request, 'Incorrect Username or password')   
            return redirect('/',{'messages':msg,})         
    else:
        return render(request,'index.html')
    
@login_required(login_url='/')
def adminpage(request):
    no_of_emp =Employees.objects.all().count()
    no_of_departments = Department.objects.all().count()
    x = Employees.objects.all()
    print(x)
    return render(request,'adminpage.html',{'empcount':no_of_emp,'departcount':no_of_departments})

@login_required(login_url='/')
def handlelogout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/')
def employees(request):
    obj = Employees.objects.all()
    fields = Employees._meta.get_fields()
    form = empform
    if request.method == "POST":
        form = empform(request.POST)
        if form.is_valid():
            print("Executed")
            form.save()
    return render(request,'employees.html',{'empobj':obj,'fields':fields,'form':form,'update_status':0})

@login_required(login_url='/')
def update_employees(request,empid):
    obj = Employees.objects.all()
    fields = Employees._meta.get_fields()
    employee = Employees.objects.get(pk=int(empid))
    form = empform(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employees')   
    return render(request,'employees.html',{'empobj':obj,'fields':fields,'employee':employee,'form':form,'update_status':1})

@login_required(login_url='/')
def update_department(request,departid):
    departobj = Department.objects.all() 
    fields = Department._meta.get_fields()
    department_data = Department.objects.get(pk=int(departid))
    form = departmentform(request.POST or None, instance=department_data)
    if form.is_valid():
        form.save()
        return redirect('department')   
    return render(request,'department.html',{'departobj':departobj,'fields':fields,'update_status':1,'form':form})

@login_required(login_url='/')
def delete_employees(request,empid):
    employee = Employees.objects.get(pk=int(empid))
    employee.delete()
    return redirect('employees')

@login_required(login_url='/')
def delete_department(request,departid):
    depart = Department.objects.get(pk=int(departid))
    depart.delete()
    return redirect('department')
    
@login_required(login_url='/')
def department(request):
    departobj = Department.objects.all() 
    fields = Department._meta.get_fields()
    if request.method == "POST":
        depart_name = request.POST.get('departmentname')
        status = request.POST.get('status')
        depart = Department(Department_name = depart_name,Status=status)
        depart.save()
        try:
            pass
        except:
            pass
        
    return render(request,'department.html',{'departobj':departobj,'fields':fields})

