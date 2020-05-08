from django.urls import path
from .views import (
    index, art, profiles, profile, make, puppetry, videos, login_, register_, contact, news, comments,
    logout_view)

urlpatterns = [
    path('', index, name="index"),
    path('art/', art, name="art"),
    path('profiles/', profiles, name="profiles"),
    path('profile/<int:num>/', profile, name="profile"),
    path('make/', make, name="make"),
    path('puppetry/', puppetry, name="puppetry"),
    path('videos/', videos, name="videos"),
    path('login/', login_, name="login"),
    path('register/', register_, name="register"),
    path("contact/", contact, name="contact"),
    path("news/<int:num>/", news, name="news"),
    path("comments/<int:num>/", comments, name="comment"),
    path("logout/", logout_view, name="logout")
]