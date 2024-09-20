from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.gis.db.models.functions import Distance
from ..models import Station
from .serializers import StationSerializer, CreateStationSerializer


class CreateStationView(generics.CreateAPIView):
    serializer_class = CreateStationSerializer
    queryset = Station.objects.all()

    def post(self, request):
        serializer = CreateStationSerializer(data=request.data)
        if serializer.is_valid():
            station = serializer.save()
            return Response({
                'id': station.id,
                'name': station.name,
                'ubication': station.ubication.coords
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListStationView(generics.ListAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset
    

class ListNearStationView(generics.RetrieveAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

    def get(self, request, pk):
        try:
            station_current = Station.objects.get(id=pk)
            stations = Station.objects.exclude(id=pk).annotate(
                distancia=Distance('ubication', station_current.ubication)
            ).order_by('distancia')
            station_near = stations.first()
            if station_near:
                serializer = StationSerializer(station_near)
                return Response(serializer.data)
            return Response({"error": "There are no other stations"}, status=status.HTTP_404_NOT_FOUND)
        except Station.DoesNotExist:
            return Response({"error": "Station Not Found"}, status=status.HTTP_404_NOT_FOUND)