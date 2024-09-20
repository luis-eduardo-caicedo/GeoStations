from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import Point

class Station(models.Model):
    name = models.CharField(max_length=100)
    ubication = gis_models.PointField(geography=True, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.latitude is not None and self.longitude is not None:
            self.ubication = Point(self.longitude, self.latitude, srid=4326)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name