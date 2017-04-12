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
from django.contrib import admin
from django.contrib.auth import views as auth_view
from blog import views
from django.core.urlresolvers import set_script_prefix
from haw358.settings import SITE_URL
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', views.index),
    url(r'^home[.]html', views.home, None, 'home'),
    url(r'^blog/$', views.blog, None, 'blog'),
    url(r'^blog/(\d+)/(\d+)/(\w+)[.]html', views.view_blog, None, 'view_blog'),
    url(r'^image/$', views.image, None, 'image'),
    url(r'^admin/write_blog/(.*)$', views.write_blog, None, 'write_blog'),
    url(r'^admin/save_blog/$', views.save_blog, None, 'save_blog'),
    url(r'^admin/list/$', views.admin_list, None, 'admin_list'),
    url(r'^admin/delete/(\d+)$', views.delete, None, 'admin_delete'),
    url(r'^login/$', auth_view.login, None, 'login'),
    url(r'^logout/$', auth_view.logout, None, 'logout')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

set_script_prefix(SITE_URL)
