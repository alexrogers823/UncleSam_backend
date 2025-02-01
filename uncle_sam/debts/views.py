from debts.models import Debt
from debts.serializers import DebtSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def debt_list(request):
    if request.method == 'GET':
        debts = Debt.objects.all()
        serializer = DebtSerializer(debts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DebtSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

@csrf_exempt
def debt_detail(request, pk):
    try:
        debt = Debt.objects.get(pk=pk)
    except Debt.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = DebtSerializer(debt)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DebtSerializer(debt, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        debt.delete()
        return HttpResponse(status=204)
