from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book
from books.serializers import getBook_serializer

class AddToFavourites(APIView):
    def post(self, request, *args, **kwargs):
        fav_book = Book.objects.get(id=request.data['book_id'])
        request.user.favourites.add(fav_book)
        return Response(status=status.HTTP_201_CREATED)

class RemoveFromFavourites(APIView):
    def delete(self, request, *args, **kwargs):
        fav_book = Book.objects.get(id=request.data['book_id'])
        request.user.favourites.remove(fav_book)
        return Response(status=status.HTTP_201_CREATED)

class GetFavourites(APIView):
    def get(self, request, *args, **kwargs):
        books= request.user.favourites.all()
        serializer = getBook_serializer(books, many=True)
        return Response(serializer.data)

