from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import TransportOption, HotelOption, GuideOption, Package
from .serializers import (
    TransportOptionSerializer,
    HotelOptionSerializer,
    GuideOptionSerializer,
    PackageSerializer,
    PackageCreateSerializer
)


class TransportOptionListView(ListAPIView):
    queryset = TransportOption.objects.all()
    serializer_class = TransportOptionSerializer


class HotelOptionListView(ListAPIView):
    queryset = HotelOption.objects.all()
    serializer_class = HotelOptionSerializer


class GuideOptionListView(ListAPIView):
    queryset = GuideOption.objects.all()
    serializer_class = GuideOptionSerializer


class PackageCreateView(CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCreateSerializer
    permission_classes = [IsAuthenticated]
