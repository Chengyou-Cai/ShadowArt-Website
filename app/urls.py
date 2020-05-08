from django.conf.urls import url #Django中所有路由映射由该函数生成
from . import views

#关键变量urlpatterns保存由所有url()函数生成的路由映射
urlpatterns = [
    url(r'mi',views.moment_input,name='app.mi'),
    url(r'show',views.show),
    url(r'',views.welcome,name='app.views.welcome'),
]