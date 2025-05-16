from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer


@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful", "is_staff": user.is_staff}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=401)


@method_decorator(csrf_exempt, name='dispatch')
class Register(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User registered successfully", status=200)
        return Response(serializer.errors, status=400)
