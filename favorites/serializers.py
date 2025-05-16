from rest_framework import serializers
from .models import  Favorites

class Favorites_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['favorite_id', 'user_id', 'book_id']



