# Generated by Django 4.2.16 on 2024-09-20 05:49

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0002_station_latitude_station_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='ubication',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
