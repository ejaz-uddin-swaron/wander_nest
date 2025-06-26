from django.urls import path
from .views import PackageSearchView, FeatureDestinationListView

urlpatterns = [
    path("search/", PackageSearchView.as_view(), name="package-search"),
    path("feature-destinations/", FeatureDestinationListView.as_view(), name="feature-destination-list"),
]
