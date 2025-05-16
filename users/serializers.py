from rest_framework import serializers
from .models import Users

class LoginSerializers(serializers.ModelSerializer) :
    class Meta:
        model = Users
        fields = ['username', 'password']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'is_staff']

    def create(self, validated_data):
        is_staff = validated_data.pop('is_staff')
        user = Users.objects.create_user(**validated_data)
        user.is_staff = is_staff
        user.save()
        return user