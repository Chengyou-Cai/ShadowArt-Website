"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#path与url是两个不同的模块的函数，效果都是响应返回页面，
#path用于映射第三方模块或者框架，url用于自定义的模块的函数
from django.conf.urls import url,include

urlpatterns = [
    #正则表达式，所有以app开头的路由(形如app/first)，通过include()函数转接到app.urls
    url(r'^app/',include('app.urls')),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
