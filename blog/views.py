from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template.loader import *
from django.contrib.auth.decorators import login_required
from .form import LoginForm
from .models import Blog, Category
# from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
import json
import datetime


# Create your views here.
def login(request):
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


def render_container(content_middle, beta_content):
    content = render_to_string('module/content.tpl', context={'content_middle': content_middle, 'beta_content': beta_content})
    header = render_to_string('module/header.tpl')
    footer = render_to_string('module/footer.tpl', context={'current_year': datetime.datetime.now().year})
    return render_to_string('module/container.tpl', context={'header': header, 'content': content, 'footer': footer})


def blog(request):
    blogs = Blog.objects.all()
    blog_list = render_to_string('blog/blog_list.html', context={'blogs': blogs}, request=request)
    aside = render_to_string('blog/aside.html')

    container = render_container(blog_list, aside)
    return render(request, 'blog/blog.html', {'container': container})


def view_blog(request, year, month, route_name):
    blog = Blog.objects.filter(add_time__year=year, add_time__month=month, route_name=route_name).first()
    pre_blog = Blog.objects.filter(add_time__lt=blog.add_time).last()
    next_blog = Blog.objects.filter(add_time__gt=blog.add_time).first()
    near_blogs = list()
    near_blogs.append(pre_blog)
    near_blogs.append(next_blog)
    blog_content = render_to_string('view_blog/blog_content.html', context={'near_blogs': near_blogs, 'blog': blog})

    container = render_container(blog_content, '')
    return render(request, 'view_blog/view_blog.html', {'container': container, 'blog': blog})


@login_required
# @csrf_exempt
def write_blog(request, blog_id):
    blog = None
    if blog_id:
        blog = Blog.objects.get(id=blog_id)
    category = Category.objects.all()
    csrf_token = csrf(request).get('csrf_token')
    return render(request, 'write_blog/write_blog.html', {'csrf_token': csrf_token, 'category': category, 'blog': blog})


@login_required
# @csrf_exempt
def save_blog(request):
    id = request.POST.get('id')
    route_name = request.POST.get('route_name')
    title = request.POST.get('title')
    category_id = request.POST.get('category_id')
    content = request.POST.get('content')

    if id:
        blog = Blog.objects.get(id=id)
        blog.title = title
        blog.content = content
        blog.save()
        return HttpResponse(json.dumps({'result': True}), content_type="application/json")

    now = datetime.datetime.now()
    blog = Blog.objects.filter(add_time__year=now.year, add_time__month=now.month, route_name=route_name).first()
    if blog:
        return HttpResponse(json.dumps({'result': False}), content_type="application/json")

    blog = Blog()
    blog.route_name = route_name
    blog.title = title
    blog.content = content
    cgy = Category.objects.get(id=category_id)
    blog.category = cgy
    blog.save()
    return HttpResponse(json.dumps({'result': True}), content_type="application/json")


@login_required
# @csrf_exempt
def delete(request, id):
    item = Blog.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect('/blog')


def image(request):
    return render(request, 'demo/image.html')


@login_required
def admin_list(request):
    return render(request, 'admin/admin.html')
