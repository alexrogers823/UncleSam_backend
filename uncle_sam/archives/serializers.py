from archives.models import Archive
from rest_framework import serializers


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ['type', 'title', 'amount', 'updated_date']