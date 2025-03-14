from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(requiste):
    return HttpResponse("hello sir this is my frist django project")

def home(request):
    return HttpResponse("hello this is my about area")
    
