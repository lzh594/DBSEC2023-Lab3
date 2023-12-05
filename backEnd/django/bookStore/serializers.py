# _*_ coding: utf-8 _*_
"""
Time:     2023/12/1
Author:   刘征昊(£·)
Version:  V 1.1
File:     serializers
Describe: 
"""
from rest_framework import serializers

from .models import Users, Authors, Publishers, Category, Books, Shoppingcarts, Shoppinghistory, Collection


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Authors.objects.all())
    publishers = serializers.PrimaryKeyRelatedField(queryset=Publishers.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Books
        fields = '__all__'


class ShoppingcartsSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Shoppingcarts
        fields = '__all__'


class ShoppinghistorySerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Shoppinghistory
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())

    class Meta:
        model = Collection
        fields = '__all__'
