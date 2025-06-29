from django.urls import path
from .views import PackageListView

urlpatterns = [
    path("all/", PackageListView.as_view(), name="package-list"),
]
