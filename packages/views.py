from home.models import FeatureDestination
from home.serializers import FeatureDestinationSerializer
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from difflib import get_close_matches

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FeatureDestinationListView(ListAPIView):
    queryset = FeatureDestination.objects.all()
    serializer_class = FeatureDestinationSerializer


class PackageSearchView(APIView):
    @swagger_auto_schema(
        operation_summary="Search location",
        operation_description="Returns the closest matching location name based on user input.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["location"],
            properties={
                "location": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Partial or full location name to search",
                    example="cox"
                ),
            },
        ),
        responses={
            200: openapi.Response(
                description="Closest matching location found",
                examples={
                    "application/json": {
                        "closest_location": "Cox's Bazar"
                    }
                }
            ),
            404: openapi.Response(
                description="No similar location found",
                examples={
                    "application/json": {
                        "message": "No similar location found"
                    }
                }
            )
        }
    )
    def post(self, request):
        location = request.data.get("location", "").lower()
        all_titles = FeatureDestination.objects.values_list("title", flat=True)
        matches = get_close_matches(location, all_titles, n=1, cutoff=0.4)

        if matches:
            return Response({"closest_location": matches[0]}, status=status.HTTP_200_OK)
        return Response({"message": "No similar location found"}, status=status.HTTP_404_NOT_FOUND)
