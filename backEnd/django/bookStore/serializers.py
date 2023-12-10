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
    authors = AuthorsSerializer(read_only=True)
    author_id = PrimaryKeyRelatedField(queryset=Authors.objects.all(), write_only=True, help_text="作者序号")
    publishers = PublishersSerializer(read_only=True)
    pub_id = PrimaryKeyRelatedField(queryset=Publishers.objects.all(), write_only=True, help_text="出版社序号")
    category = CategorySerializer(read_only=True)
    category_id = PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, help_text="种类序号")

    class Meta:
        model = Books
        fields = '__all__'


class ShoppingcartsSerializer(ModelSerializer):
    user = UsersSerializer(read_only=True)
    uid = PrimaryKeyRelatedField(queryset=Shoppingcarts.objects.all(), write_only=True, help_text="用户序号")
    book = BooksSerializer(read_only=True)
    book_id = PrimaryKeyRelatedField(queryset=Shoppingcarts.objects.all(), write_only=True, help_text="书的序号")

    class Meta:
        model = Shoppingcarts
        fields = '__all__'


class ShoppinghistorySerializer(ModelSerializer):
    user = UsersSerializer(read_only=True)
    uid = PrimaryKeyRelatedField(queryset=Shoppingcarts.objects.all(), write_only=True, help_text="用户序号")
    book = BooksSerializer(read_only=True)
    book_id = PrimaryKeyRelatedField(queryset=Shoppingcarts.objects.all(), write_only=True, help_text="书的序号")

    class Meta:
        model = Shoppinghistory
        fields = '__all__'


class CollectionSerializer(ModelSerializer):
    user = UsersSerializer(read_only=True)
    uid = PrimaryKeyRelatedField(queryset=Shoppingcarts.objects.all(), write_only=True, help_text="用户序号")
    book = BooksSerializer(read_only=True)
    book_id = PrimaryKeyRelatedField(queryset=Shoppingcarts.objects.all(), write_only=True, help_text="书的序号")

    class Meta:
        model = Collection
        fields = '__all__'
