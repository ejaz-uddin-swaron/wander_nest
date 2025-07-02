from rest_framework import serializers
from .models import HeroSection, FeatureDestination, OurService, Destination

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class FeatureDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureDestination
        fields = ['id', 'title', 'subtitle', 'image_url', 'large_description']

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__'
