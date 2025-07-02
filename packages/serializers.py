# packages/serializers.py

from rest_framework import serializers
from home.models import FeatureDestination

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureDestination
        fields = ['id', 'title', 'subtitle', 'image_url', 'price']