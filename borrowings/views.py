from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book
from books.serializers import getBook_serializer

# Create your views here.


class BorrowBook(APIView):
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(id = request.data['book_id'])
        if book.user is None:
            book.user = request.user
            book.save()
            return Response({"message": "Book borrowed successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Book already borrowed"}, status=status.HTTP_400_BAD_REQUEST)

class GetBorrowings(APIView):
    def get(self, request, *args, **kwargs):
        books = request.user.books.all()
        books_serializer = getBook_serializer(books, many=True)
        return Response(books_serializer.data, status=status.HTTP_200_OK)


class ReturnBook(APIView):
    def post(self, request, *args, **kwargs):
        book = Book.objects.get(id = request.data['book_id'])
        if book.user is not None:
            book.user = None
            book.save()
            return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Book already in-shelf"}, status=status.HTTP_400_BAD_REQUEST)