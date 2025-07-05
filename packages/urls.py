from django.urls import path
from .views import (
    TransportOptionListView,
    HotelOptionListView,
    GuideOptionListView,
    PackageCreateView,
    PreMadePackageListView
)

urlpatterns = [
    path('transport-options/', TransportOptionListView.as_view()),
    path('hotel-options/', HotelOptionListView.as_view()),
    path('guide-options/', GuideOptionListView.as_view()),
    path('create/', PackageCreateView.as_view()),
    path('all/', PreMadePackageListView.as_view(), name='premade-packages'),
]
