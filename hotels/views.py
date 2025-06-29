# hotels/views.py

from rest_framework.generics import ListAPIView
from .models import Hotel
from .serializers import HotelSerializer

class HotelListView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
