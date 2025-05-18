from django.contrib.auth import get_user_model

from rest_framework import serializers

from books.models import Book

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username' ,'total_borrowings','total_returns']
        #allah y5rbeet django

# class getBook_serializer (serializers.ModelSerializer) :
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'category', 'language', 'description', 'image', 'user']
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if representation['user'] is None:
#             representation['is_borrowed'] = False
#         else:
#             representation['is_borrowed'] = True
#         return representation
# from rest_framework import serializers
# from .models import Book  # or wherever your Book model is defined
#
# class BorrowedBookSerializer(serializers.ModelSerializer):
#     last_login = serializers.DateTimeField(source='user.last_login', read_only=True)
#
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'category', 'user', 'last_login']
#

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

