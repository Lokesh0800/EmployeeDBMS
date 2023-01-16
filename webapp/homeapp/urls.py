from unicodedata import name
from django.contrib import admin
from django.urls import path
from homeapp import views

urlpatterns = [
    path('',views.Login,name='Login'),
    path('home',views.index,name='home'),
    path('DataEntry',views.entry_form,name='entry_form'),
    path('DataAccess',views.access_form,name='access_form'),
    path('DataDeletion',views.delete_form,name='delete_form'),
    path('convertToCSV',views.csv_convertion,name='csv_convertion'),
    path('Login',views.Login,name='Login')
]
