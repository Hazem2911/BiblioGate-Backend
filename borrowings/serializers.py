from rest_framework import serializers
from .models import borrowings

class borrowings_serializer (serializers.ModelSerializer) :
    class Meta:
        model = borrowings
        fields = ['borrowings_id', 'user_id', 'book_id']
