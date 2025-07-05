from django.urls import path
from .views import (
    TransportOptionListView,
    HotelOptionListView,
    GuideOptionListView,
    PackageCreateView,
    PreMadePackageListView
)

urlpatterns = [
    path('api/packages/transport-options/', TransportOptionListView.as_view()),
    path('api/packages/hotel-options/', HotelOptionListView.as_view()),
    path('api/packages/guide-options/', GuideOptionListView.as_view()),
    path('api/packages/create/', PackageCreateView.as_view()),
    path('all/', PreMadePackageListView.as_view(), name='premade-packages'),
]
