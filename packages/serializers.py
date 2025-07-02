# packages/serializers.py

from rest_framework import serializers
from home.models import FeatureDestination

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureDestination
        fields = ['id', 'title', 'subtitle', 'large_description', 'image_url', 'price']