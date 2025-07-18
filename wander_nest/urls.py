from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Wander Nest API",
      default_version='v1',
      description="API documentation for the Wander Nest project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/auth/', include('authentication.urls')),
   path('api/home/', include('home.urls')),
   path("api/packages/", include('packages.urls')),
   path('api/flights/', include('flights.urls')),
   path('api/bookings/', include('bookings.urls')),
   path('api/currency/', include('currency.urls')),
   path('api/hotels/', include('hotels.urls')),
   path('api/', include('restaurants.urls')),
   path('initiate-payment/', include('payments.urls')),
   path('api/', include('reviews.urls')),
   path('api/', include('trips.urls')),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
