from rest_framework import serializers
from savings.models import Saving


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = ['id', 'title', 'priority', 'current_amount', 'goal', 'updated', 'goal_date']