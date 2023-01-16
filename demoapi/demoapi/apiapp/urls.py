
from django.urls import path,include
from apiapp import views

urlpatterns = [
    
    path("",views.index,name="index"),
    path("getdata",views.getdata,name="getdata"),
    path("<int:id>",views.dataapi,name="dataapi"),
    path('api-getdata',views.apidata,name='apidata'),
    #path("createdata",views.createdata,name="createdata"),
    
]
