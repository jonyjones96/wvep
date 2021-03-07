from django.test import TestCase
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welsh Valley Engineering Project<\h1>')

