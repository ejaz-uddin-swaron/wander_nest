from django.urls import path
from .views import CurrencyRateAPIView

urlpatterns = [
    path('rates/', CurrencyRateAPIView.as_view(), name='currency-rates'),
]
