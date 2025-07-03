from django.urls import path
from .views import FlightSearchView, FlightDetailView, AirportListView

urlpatterns = [
    path('search/', FlightSearchView.as_view(), name='flight-search'),
    path('airports/', AirportListView.as_view(), name='airport-list'),
    path('<str:flight_id>/', FlightDetailView.as_view(), name='flight-detail'),  # KEEP LAST!
]
