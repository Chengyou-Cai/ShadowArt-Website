from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import os
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.urls.base import reverse #Django2.0 将django.core.urlresolvers 包 更改为了 django.urls包

from .models import Moment

def welcome(request):
    return HttpResponse("<h1>Hello<h1>")

def show(request):
    show_list=Moment.objects.all()
    string="<h1>{}</h1>".format(show_list[0])
    return HttpResponse(string)

@csrf_exempt
def moment_input(request):
    if request.method=='POST': #用户提交POST表单，则保存moment对象，并重定向到欢迎页面
        form=MomentForm(request.POST)
        if form.is_valid():
            moment=form.save()
            moment.save()
            return HttpResponseRedirect('/app/show')
    else: #否则返回模板渲染结果作为HTTP Response
        form=MomentForm()
    PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,os.path.join(PROJECT_ROOT,'app/templates','moments_input.html'),{'form':form})
