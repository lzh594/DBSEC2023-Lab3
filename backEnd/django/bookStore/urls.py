# _*_ coding: utf-8 _*_
"""
Time:     2023/11/30
Author:   刘征昊(£·)
Version:  V 1.1
File:     urls
Describe: 
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]