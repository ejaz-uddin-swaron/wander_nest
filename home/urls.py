from django.urls import path
from .views import HeroSectionView, FeatureDestinationView, OurServiceView, DestinationListView, increment_click

urlpatterns = [
    path('hero/', HeroSectionView.as_view()),
    path('features/', FeatureDestinationView.as_view()),
    path('services/', OurServiceView.as_view()),
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/click/', increment_click, name='destination-click'),
]
