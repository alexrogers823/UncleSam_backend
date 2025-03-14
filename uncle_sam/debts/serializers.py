from debts.models import Debt
from rest_framework import serializers


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt 
        exclude = ['created']