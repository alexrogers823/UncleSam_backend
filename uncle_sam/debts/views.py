from debts.models import Debt
from debts.serializers import DebtSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DebtList(APIView):
    def get(self, request, format=None) -> Response:
        debts = Debt.objects.all()
        serializer = DebtSerializer(debts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None) -> Response:
        serializer = DebtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DebtDetail(APIView):
    def get_object(self, pk) -> Debt:
        try:
            return Debt.objects.get(pk=pk)
        except Debt.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None) -> Response:
        debt = self.get_object(pk)
        serializer = DebtSerializer(debt)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None) -> Response:
        debt = self.get_object(pk)
        serializer = DebtSerializer(debt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None) -> Response:
        debt = self.get_object(pk)
        debt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
