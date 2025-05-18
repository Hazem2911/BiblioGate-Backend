from django.contrib.auth import get_user_model
from rest_framework import serializers
from books.models import Book

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username' ,'total_borrowings','total_returns']

class BorrowedBookSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(source='user.last_login', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'user', 'last_login']

class AvailableBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'category']


class UserBorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'category']

