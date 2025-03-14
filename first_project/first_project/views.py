from django.http import HttpResponse

def home(request):
    return HttpResponse("hello dhaka this is my first django project") 

def about(request):
    return HttpResponse("<h1>this is my about page</h1>")