from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HeroSection, FeatureDestination, OurService
from .serializers import HeroSectionSerializer, FeatureDestinationSerializer, OurServiceSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class HeroSectionView(APIView):

    @swagger_auto_schema(
        operation_description="Returns hero section details (title, subtitle, background_image)",
        responses={200: openapi.Response(
            description="Success",
            examples={
                "application/json": {
                    "title": "Welcome to Wander Nest",
                    "subtitle": "Explore the world",
                    "background_image": "http://example.com/image.jpg"
                }
            }
        )}
    )

    def get(self, request):
        hero = HeroSection.objects.all()
        serializer = HeroSectionSerializer(hero, many=True)
        return Response(serializer.data)

class FeatureDestinationView(APIView):
    def get(self, request):
        features = FeatureDestination.objects.all()
        serializer = FeatureDestinationSerializer(features, many=True)
        return Response(serializer.data)

class OurServiceView(APIView):
    def get(self, request):
        services = OurService.objects.all()
        serializer = OurServiceSerializer(services, many=True)
        return Response(serializer.data)
