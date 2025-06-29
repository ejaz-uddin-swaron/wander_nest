# hotels/urls.py

from django.urls import path
from .views import HotelListView

urlpatterns = [
    path('', HotelListView.as_view(), name="hotel-list"),
]
