from django.shortcuts import render
from django.conf.urls import url
from . import views

# Create your views here.

urlpatterns=[
  url(r'^$',views.welcome, name = 'welcome'),
]