from django.shortcuts import render
from django.http import HttpResponse
import requests
import os

def home(request): 
    #response = requests.get('http://{}:8080/tools'.format(host))
    response = requests.get('http://localhost:5000/supplies')
    suppliesJson = response.json() 
    return render(request, 'website/home.html',{'supplies': suppliesJson})

def getItem(request,id):
    response = requests.get('http://localhost:5000/supplies/item/{}'.format(id))
    itemInfo = response.json()
    return render(request, 'website/displayItem.html', {'Item': itemInfo})

def getBasket(request):
    return render(request,'website/basket.html')

def getTracking(request):
    return render(request,'website/tracker.html')
