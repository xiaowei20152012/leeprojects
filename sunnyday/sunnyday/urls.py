"""sunnyday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sunuser import views as user_view
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',user_view.index,name='user_index'),
    url(r'^user/examples',user_view.userexmaple,name='examples'),
    url(r'^user/register',user_view.register,name='user_register'),
    url(r'^user/login',user_view.login,name='user_login'),
    url(r'^user/forget',user_view.forget,name='user_forget'),
    url(r'^user/getNews',user_view.getNews,name='user_getnews'),
    url(r'^Apiv2/user/getUser',user_view.getUser,name='user_getuser'),

]
