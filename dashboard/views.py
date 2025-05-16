from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dashboard.serializers import UserSerializer

# Create your views here.


User = get_user_model()

class usersTable(APIView):
    def get(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        username = request.query_params.get('username')

        filters = {}
        if id:
            filters['id'] = id
        if username:
            filters['username__icontains'] = username

        users = User.objects.filter(**filters)
        userSerializer = UserSerializer(users, many=True)

        return Response(userSerializer.data, status=status.HTTP_200_OK)
