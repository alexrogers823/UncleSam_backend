from rest_framework import serializers
from savings.models import Saving


class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        exclude = ['created']