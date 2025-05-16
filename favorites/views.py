from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from favorites.models import Favorites
from favorites.serializers import Favorites_Serializer

class AddFavorites(APIView):
    def post(self, request, *args, **kwargs):
        serializer = Favorites_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added Book to favorites Successfully", status=200)
        return Response(serializer.errors, status=400)

class GetFavorites(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        if user_id:
            try:
                favorites = Favorites.objects.filter(user_id=user_id)
                serializer = Favorites_Serializer(favorites, many=True)
                return Response(serializer.data, status=200)
            except Favorites.DoesNotExist:
                return Response({"error": "Favorites not found"}, status=404)
        else:
            favorites = Favorites.objects.all()
            serializer = Favorites_Serializer(favorites, many=True)
            return Response(serializer.data, status=200)

class DeleteFavorites(APIView):
    def delete(self, request, *args, **kwargs):
        favorite_id = kwargs.get('favorite_id')
        if favorite_id:
            try:
                favorite = Favorites.objects.get(id=favorite_id)
                serializer = Favorites_Serializer(favorite)
                favorite.delete()
                return Response({
                    "message": "Favorite deleted successfully",
                    "deleted_favorite": serializer.data
                }, status=200)
            except Favorites.DoesNotExist:
                return Response({"error": "Favorite not found"}, status=404)
        else:
            return Response({"error": "Favorite ID is required"}, status=400)