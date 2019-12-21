
from django.conf.urls import url
from django.urls import path, re_path
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
]