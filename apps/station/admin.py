from django import forms
from django.contrib import admin
from django.contrib.gis import forms as gis_forms
from .models import Station

class StationAdminForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = '__all__'
        widgets = {
            'ubication': gis_forms.OSMWidget(attrs={
                'map_width': '800px',
                'map_height': '400px',
            }),
        }

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    form = StationAdminForm
    list_display = ('name', 'ubication')