from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HeroSection, FeatureDestination, OurService, Destination
from .serializers import HeroSectionSerializer, FeatureDestinationSerializer, OurServiceSerializer, DestinationSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework import status

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
    

class DestinationListView(APIView):

    @swagger_auto_schema(
        operation_description="Returns all available destinations (name, image, description, click count)",
        responses={200: openapi.Response(
            description="Success",
            examples={
                "application/json": [
                    {
                        "name": "Sylhet",
                        "image": "http://example.com/media/destination_images/srimangal.png",
                        "description": "Discover lush tea gardens, rolling hills, and indigenous tribal cultures.",
                        "click": 9
                    }
                ]
            }
        )}
    )
    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def increment_click(request, pk):
    try:
        destination = Destination.objects.get(pk=pk)
        destination.click += 1
        destination.save()
        serializer = DestinationSerializer(destination)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)
