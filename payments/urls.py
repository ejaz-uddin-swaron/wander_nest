from django.urls import path
from .views import SSLCommerzPaymentView

urlpatterns = [
    path('', SSLCommerzPaymentView.as_view(), name='initiate-payment'),
]
