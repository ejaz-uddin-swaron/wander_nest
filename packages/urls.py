from django.urls import path
from .views import (
    TransportOptionListView,
    HotelOptionListView,
    GuideOptionListView,
    PackageCreateView
)

urlpatterns = [
    path('api/packages/transport-options/', TransportOptionListView.as_view()),
    path('api/packages/hotel-options/', HotelOptionListView.as_view()),
    path('api/packages/guide-options/', GuideOptionListView.as_view()),
    path('api/packages/create/', PackageCreateView.as_view()),
]
