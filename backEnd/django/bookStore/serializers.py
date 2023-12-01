# _*_ coding: utf-8 _*_
"""
Time:     2023/12/1
Author:   刘征昊(£·)
Version:  V 1.1
File:     serializers
Describe: 
"""
from rest_framework import serializers

from bookStore.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
