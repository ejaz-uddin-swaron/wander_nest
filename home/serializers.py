from rest_framework import serializers
from .models import HeroSection, FeatureDestination, OurService

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class FeatureDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureDestination
        fields = ['id', 'title', 'subtitle', 'pic']

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__'
