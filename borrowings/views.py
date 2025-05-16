
from rest_framework.response import Response
from rest_framework.views import APIView

from borrowings.serializers import borrowings_serializer

# Create your views here.



class Borrowingsbooks(APIView):
    def post(self, request, *args, **kwargs):
        serializer = borrowings_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added Book to borrowings Successfully", status=200)
        return Response(serializer.errors, status=400)