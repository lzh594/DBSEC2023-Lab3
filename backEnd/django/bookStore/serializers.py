# _*_ coding: utf-8 _*_
"""
Time:     2023/12/1
Author:   刘征昊(£·)
Version:  V 1.1
File:     serializers
Describe: 
"""
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from .models import Users, Authors, Publishers, Category, Books, Shoppingcarts, Shoppinghistory, Collection


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class PublishersSerializer(ModelSerializer):
    class Meta:
        model = Publishers
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(queryset=Authors.objects.all())
    publishers = PrimaryKeyRelatedField(queryset=Publishers.objects.all())
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Books
        fields = '__all__'


class ShoppingcartsSerializer(ModelSerializer):
    book = PrimaryKeyRelatedField(queryset=Books.objects.all())
    user = PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Shoppingcarts
        fields = '__all__'


class ShoppinghistorySerializer(ModelSerializer):
    book = PrimaryKeyRelatedField(queryset=Books.objects.all())
    user = PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Shoppinghistory
        fields = '__all__'


class CollectionSerializer(ModelSerializer):
    book = PrimaryKeyRelatedField(queryset=Books.objects.all())
    user = PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Collection
        fields = '__all__'
