from django.shortcuts import render
from django.http import HttpResponse
import requests
import os

def home(request): 
    #response = requests.get('http://{}:8080/tools'.format(host))
    host = os.environ.get('HOST') 
    response = requests.get('http://{}:5000/supplies'.format(host))
    suppliesJson = response.json() 
    return render(request, 'website/home.html',{'supplies': suppliesJson})

def getItem(request,id):
    host = os.environ.get('HOST') 
    response = requests.get('http://{}:5000/supplies/item/{}'.format(host,id))
    itemInfo = response.json()
    return render(request, 'website/displayItem.html', {'Item': itemInfo})

def getBasket(request):
    return render(request,'website/basket.html')

def getTracking(request):
    return render(request,'website/tracker.html')
