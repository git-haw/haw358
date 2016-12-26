from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    # request.GET
    # request.POST
    # return HttpResponse("hello world!")
    return render(request, "index.html", )