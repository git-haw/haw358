from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template.loader import *
# from django.contrib.auth.decorators import login_required
from .form import LoginForm
from .models import Blog
from django.views.decorators.csrf import csrf_exempt
from haw358.settings import BASE_DIR
import os


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
    nav_bar = render_to_string('blog/nav_bar.html')
    blog = Blog.objects.all()
    blog_list = render_to_string('blog/blog_list.html', context={'blog': blog})
    return render(request, 'blog/blog.html', {'nav_bar': nav_bar, 'content_middle': blog_list})


def write_blog(request):
    nav_bar = render_to_string('blog/nav_bar.html')
    write_blog = render_to_string('blog/write_blog2.html')
    return render(request, 'blog/blog.html', {'nav_bar': nav_bar, 'content_middle': write_blog})


@csrf_exempt
def save_blog(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    blog = Blog()
    blog.title = title
    blog.content = content
    blog.save()
    return HttpResponseRedirect('/blog/')


@csrf_exempt
def delete(request):
    id = request.POST.get('id')
    blog = Blog.objects.get(id=id)
    blog.delete()


def query(request):
    id = request.POST.get('id')
    blog = Blog.objects.get(id=id)
