from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

from .forms import CommentForm
from .forms import RegistrationForm
from .models import PYnews
from .models import Comments

def index(request):
    return render(request, "index.html")

def art(request):
    return render(request, "art.html")

def profiles(request):
    return render(request, "profiles.html")

def profile(request, num):
    comments = Comments.objects.all().filter(article=num)
    return render(request, "profile"+ str(num) + ".html", {'num':num, 'comments':comments})


def make(request):
    return render(request, "make.html")

def puppetry(request):
    return render(request, "puppetry.html")
def videos(request):
    print(request.method)
    return render(request, "videos.html")

def login_(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/news/1")
        else:
            return HttpResponse("用户名或者密码错误")

# def register_(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/news/1")
#         # else:
#         return render(request, "register.html", {'form': form})
#     else:
#         form = UserCreationForm()
#
#         return render(request, "register.html", {'form': form})

def register_(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("/news/1")

        return render(request, "register.html", {'form': form})
    else:
        form = RegistrationForm()

        return render(request, "register.html", {'form': form})


def contact(request):
    print(request.user.username)
    return render(request, "contact.html")


def news(request, num):
    news_list = PYnews.objects.all()
    paginator = Paginator(news_list, 8)  #
    page_num = paginator.num_pages
    page = paginator.get_page(num)
    return render(request, "news.html", {'page_range':range(1, page_num+1), "page":page,"current_page":num})


@login_required
@require_http_methods(["POST"])
def comments(request, num):

    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment_obj = comment_form.save(commit=False)
        comment_obj.posted_by = request.user.username
        comment_obj.article = num
        comment_obj.save()
        return redirect("/profile/"+str(num))
    else:
        return HttpResponseBadRequest()

def logout_view(request):
    logout(request)
    return redirect("/news/1")