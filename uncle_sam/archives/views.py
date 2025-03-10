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
    

class ArchiveChartList(APIView):
    def arrange_chart_data(self, serializer_data):
        chart_types = ["Debt", "Saving", "Item"]
        def get_chart_data(chart_name):
            titles = set([archive["title"] for archive in serializer_data if archive["type"] == chart_name])

            return map(lambda instance: {
                "title": instance,
                "history": map(lambda h: {
                    "amount": h["amount"],
                    "date": h["updated_date"]
                }, filter(lambda t: t["title"] == instance, filter(lambda chart: chart["type"] == chart_name, serializer_data)))
            }, titles)
            
        
        arranged = map(lambda chart_name: {
            "type": chart_name,
            "data": get_chart_data(chart_name)
        }, chart_types)

        return arranged

    def get(self, request, format=None) -> Response:
        archives = Archive.objects.all()
        serializer = ArchiveSerializer(archives, many=True)
        chart_data = self.arrange_chart_data(serializer.data)
        return Response(chart_data)