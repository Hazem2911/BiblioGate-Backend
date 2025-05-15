from rest_framework import serializers
from .models import Users

class LoginSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Users
        fields = ['username', 'password']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)