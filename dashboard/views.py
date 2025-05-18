from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from dashboard.serializers import UserSerializer, BorrowedBookSerializer, AvailableBookSerializer, \
    UserBorrowedBooksSerializer

# Create your views here.

User = get_user_model()

class usersTable(APIView):
    def get(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        username = request.query_params.get('username')

        filters = {}
        if id:
            filters['id'] = id
        if username:
            filters['username__icontains'] = username

        users = User.objects.filter(**filters)
        userSerializer = UserSerializer(users, many=True)

        return Response(userSerializer.data, status=status.HTTP_200_OK)

class BorrowedBooksTable(APIView):
    def get (self, request, *args, **kwargs):
        available_books = Book.objects.filter(user__isnull=False)
        serializer = BorrowedBookSerializer(available_books, many=True)
        return Response(serializer.data, status=200)

class AvailableBooksTable(APIView):
    def get (self, request, *args, **kwargs):
        available_books = Book.objects.filter(user__isnull=True)
        serializer = AvailableBookSerializer(available_books, many=True)
        return Response(serializer.data, status=200)

class UserBorrowedBooks(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        borrowed_books = Book.objects.filter(user=user_id)
        serializer = UserBorrowedBooksSerializer(borrowed_books, many=True)
        return Response(serializer.data)