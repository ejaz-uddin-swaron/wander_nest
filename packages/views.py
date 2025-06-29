from home.models import FeatureDestination
from home.serializers import FeatureDestinationSerializer
from rest_framework.generics import ListAPIView
from .serializers import PackageSerializer

# packages/views.py

class PackageListView(ListAPIView):
    queryset = FeatureDestination.objects.all()
    serializer_class = PackageSerializer

class FeatureDestinationListView(ListAPIView):
    queryset = FeatureDestination.objects.all()
    serializer_class = FeatureDestinationSerializer


