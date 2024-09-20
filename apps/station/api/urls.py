from django.urls import path
from .views import ListStationView, CreateStationView, ListNearStationView

urlpatterns = [
    path('list/', ListStationView.as_view(), name='list'),
    path('create/', CreateStationView.as_view(), name='create'),
    path('near/<int:pk>', ListNearStationView.as_view(), name='near'),
]