import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class CurrencyRateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        base = request.query_params.get('base_currency', 'USD')
        currencies = request.query_params.get('currencies', 'BDT,EUR')

        url = f"https://api.freecurrencyapi.com/v1/latest"
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
