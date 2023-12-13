# _*_ coding: utf-8 _*_
"""
Time:     2023/11/30
Author:   刘征昊(£·)
Version:  V 1.1
File:     urls
Describe: 
"""
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from . import views
from .views import UsersViewSet, AuthorsViewSet, PublishersViewSet, CategoryViewSet, BooksViewSet, \
    ShoppingcartsViewSet, ShoppinghistoryViewSet, CollectionViewSet

router = DefaultRouter()

router.register(r'users', UsersViewSet)
router.register(r'authors', AuthorsViewSet)
router.register(r'publishers', PublishersViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'books', BooksViewSet)
router.register(r'shoppingcarts', ShoppingcartsViewSet)
router.register(r'shoppinghistory', ShoppinghistoryViewSet)
router.register(r'collection', CollectionViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('api/', include(router.urls), name='api'),
    path('docs/', include_docs_urls(title="bookStore's api docs"), name='docs'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
