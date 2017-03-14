"""haw358 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import auth
from blog import views
from django.core.urlresolvers import set_script_prefix
from haw358.settings import SITE_URL


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.index),
    url(r'^home/', views.home, {}, 'home'),
    url(r'^blog/', views.blog, {}, 'blog'),
    url(r'^write_blog/', views.write_blog, {}, 'write_blog'),
    url(r'^save_blog/', views.save_blog, {}, 'save_blog'),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout')
]

set_script_prefix(SITE_URL)
