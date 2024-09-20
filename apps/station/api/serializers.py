from rest_framework import serializers
from ..models import Station
from django.contrib.gis.geos import Point


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name', 'ubication']


class CreateStationSerializer(serializers.ModelSerializer):
    ubication = serializers.CharField(required=True)

    class Meta:
        model = Station
        fields = ['id', 'name', 'ubication']

    def create(self, validated_data):
        ubication = validated_data.pop('ubication')
        try:
            longitude, latitude = map(float, ubication.split(','))
            validated_data['ubication'] = Point(longitude, latitude, srid=4326)
        except ValueError as e:
            raise serializers.ValidationError("Invalid format for ubication. Use 'longitude,latitude'.")
        except Exception as e:
            raise serializers.ValidationError(f"Error creating Point: {str(e)}")
        return super().create(validated_data)
