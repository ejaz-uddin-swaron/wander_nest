from django.urls import path
from .views import FlightsMapView

urlpatterns = [
    path('', FlightsMapView.as_view(), name='flights_map'),
]
