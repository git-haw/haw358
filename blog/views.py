from django.shortcuts import render
from django.shortcuts import HttpResponse
import sqlite3

# Create your views here.
def index(request):
    # request.GET
    # request.POST
    # return HttpResponse("hello world!")
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")