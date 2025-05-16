from rest_framework import serializers
from .models import Book

class addBook_serializer (serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'language', 'description', 'image']

class getBook_serializer (serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = ['id']