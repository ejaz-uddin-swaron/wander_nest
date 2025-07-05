from django.urls import path
from .views import UserTripListView

urlpatterns = [
    path('trips/', UserTripListView.as_view(), name='user-trip-list'),
]
