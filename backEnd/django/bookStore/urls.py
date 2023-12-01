# _*_ coding: utf-8 _*_
"""
Time:     2023/11/30
Author:   刘征昊(£·)
Version:  V 1.1
File:     urls
Describe: 
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'books', views.BooksViewSet)
urlpatterns = [
    # path('', views.index, name="index"),
    path('api/', include(router.urls)),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
