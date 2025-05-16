from rest_framework import serializers
from .models import Book

class addBook_serializer (serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'language', 'description', 'cover_image']

class getBook_serializer (serializers.ModelSerializer) :
    class Meta:
        model = Book
        fields = ['book_id']