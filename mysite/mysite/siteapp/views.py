from django.shortcuts import render,HttpResponse
import json
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')

def crypto(request):
    key = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

    # requesting data from url
    data = requests.get(key)
    data = data.json()
    new_data=[]
    for i in range(100):
        new_data.append(data[i])
    return render(request,'cryptopage.html',{'data':data})