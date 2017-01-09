from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
from .form import LoginForm
from .models import Blog
from django.template.loader import *

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def index(request):
    # request.GET
    # request.POST
    # return HttpResponse("hello world!")
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

# @login_required(login_url="/login/")
def blog(request):
    nav_bar = get_template('nav_bar.html')
    print(nav_bar)
    return render(request, "blog.html", {'nav_bar': nav_bar})

def write_blog(request):
    return render(request, 'blog.html')

def save_blog(request):
    blog = Blog()
    title = request.POST['title']
    content = request.POST['content']
    blog.title = title
    blog.content = content
    blog.save()
