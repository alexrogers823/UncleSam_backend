from archives.models import Archive
from archives.serializers import ArchiveSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ArchiveList(APIView):
    def get(self, request, format=None) -> Response:
        archives = Archive.objects.all()
        serializer = ArchiveSerializer(archives, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None) -> Response:
        serializer = ArchiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)