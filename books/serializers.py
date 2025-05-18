from itertools import filterfalse

from rest_framework import serializers
from .models import Book

class addBook_serializer (serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'language', 'description', 'image']

class getBook_serializer (serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'language', 'description', 'image', 'user']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['user'] is None:
            representation['is_borrowed'] = False
        else:
            representation['is_borrowed'] = True
        return representation