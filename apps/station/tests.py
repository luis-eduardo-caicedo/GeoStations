from django.test import TestCase
from django.urls import reverse
from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Station


class StationAPITests(APITestCase):
    def setUp(self):
        self.station1 = Station.objects.create(name="Station 1", ubication=Point(0, 0))
        self.station2 = Station.objects.create(name="Station 2", ubication=Point(1, 1))
        self.station3 = Station.objects.create(name="Station 3", ubication=Point(2, 2))

    def test_create_station(self):
        """
        Asegura que podemos crear una nueva estación con ubication en formato 'longitude,latitude'.
        """
        url = reverse('create')
        data = {
            'name': 'New Station',
            'ubication': '-80.1918,25.7617'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Station.objects.count(), 4)
        self.assertEqual(Station.objects.get(name='New Station').name, 'New Station')

    def test_list_stations(self):
        """
        Asegura que podemos listar todas las estaciones.
        """
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_near_station(self):
        """
        Asegura que podemos obtener la estación más cercana.
        """
        url = reverse('near', kwargs={'pk': self.station1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Station 2') 

    def test_get_near_station_not_found(self):
        """
        Asegura que obtenemos un 404 cuando la estación no existe.
        """
        url = reverse('near', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_station_invalid_data(self):
        """
        Asegura que no podemos crear una estación con datos inválidos.
        """
        url = reverse('create')
        data = {'name': '', 'ubication': {'longitude': 'invalid', 'latitude': 'invalid'}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_near_station_single_station(self):
        """
        Asegura que obtenemos un 404 cuando solo hay una estación en la base de datos.
        """
        Station.objects.all().delete()
        single_station = Station.objects.create(name="Single Station", ubication=Point(0, 0))
        url = reverse('near', kwargs={'pk': single_station.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], "There are no other stations")
