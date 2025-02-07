from django.http import Http404
from django.shortcuts import render
from items.models import Item
from items.serializers import ItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ItemList(APIView):
    def get(self, request, format=None) -> Response:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None) -> Response:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ItemDetail(APIView):
        def get_object(self, pk) -> Item:
             try:
                  return Item.objects.get(pk=pk)
             except Item.DoesNotExist:
                  raise Http404
             
        def get(self, request, pk, format=None) -> Response:
             item = self.get_object(pk)
             serializer = ItemSerializer(item)
             return Response(serializer.data)
        
        def put(self, request, pk, format=None) -> Response:
             item = self.get_object(pk)
             serializer = ItemSerializer(item, data=request.data)
             if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format=None) -> Response:
             item = self.get_object(pk)
             item.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)
