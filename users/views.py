from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Users
from .serializers import LoginSerializers, RegisterSerializer


# class Login (APIView) :
#     def post (self, request, *args, **kwargs):
#         user = authenticate(request=request , username=request.POST['username'] , password=request.POST['password'])
#         if user :
#             login(request, user)
#             return Response("OK" , status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
class login(APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])
        if user :
            login(request, user)
            return Response("OK", status=200)
        return Response(status=401)

class Register(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User registered successfully", status=200)
        return Response(serializer.errors, status=400)