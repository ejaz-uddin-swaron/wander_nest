from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.conf import settings
import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CurrencyRateAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'base_currency',
                openapi.IN_QUERY,
                description="The base currency (e.g., USD)",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'currencies',
                openapi.IN_QUERY,
                description="Comma-separated currency codes like BDT,EUR",
                type=openapi.TYPE_STRING,
                required=False
            ),
        ]
    )
    def get(self, request):
        base = request.query_params.get('base_currency', 'USD')
        currencies = request.query_params.get('currencies', 'BDT,EUR')

        url = "https://api.freecurrencyapi.com/v1/latest"
        params = {
            "apikey": settings.FREE_CURRENCY_API_KEY,
            "base_currency": base,
            "currencies": currencies
        }

        try:
            res = requests.get(url, params=params)
            data = res.json()
            return Response(data)
        except Exception as e:
            return Response({"error": "Currency fetch failed", "details": str(e)}, status=500)
