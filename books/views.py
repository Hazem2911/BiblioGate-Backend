from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book
from books.serializers import addBook_serializer
from books.serializers import getBook_serializer

class AddBook(APIView):
    def post(self,request, *args, **kwargs):
        serializer = addBook_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added Book Successfully", status=200)
        return Response(serializer.errors, status=400)

class GetBook(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('book_id')
        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                serializer = getBook_serializer(book)
                return Response(serializer.data, status=200)
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=404)
        else:
            books = Book.objects.all()
            serializer = getBook_serializer(books, many=True)
            return Response(serializer.data, status=200)

class DeleteBook(APIView):
    def delete(self, request, *args, **kwargs):
        book_id = request.data.get('book_id')
        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                book.delete()
                return Response({"message": "Book deleted successfully"}, status=200)
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=404)
        else:
            return Response({"error": "Book ID is required"}, status=400)

class EditBook(APIView):
    def put(self, request, *args, **kwargs):
        book_id = request.data.get('book_id')
        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                serializer = addBook_serializer(book, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Book updated successfully"}, status=200)
                return Response(serializer.errors, status=400)
            except Book.DoesNotExist:
                return Response({"error": "Book not found"}, status=404)
        else:
            return Response({"error": "Book ID is required"}, status=400)