from django.urls import path
from .views import HeroSectionView, FeatureDestinationView, OurServiceView

urlpatterns = [
    path('hero/', HeroSectionView.as_view()),
    path('features/', FeatureDestinationView.as_view()),
    path('services/', OurServiceView.as_view()),
]
