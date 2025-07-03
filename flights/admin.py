from django.contrib import admin
from .models import Airport, Airline, Aircraft, Flight, FlightSearch, FlightAnalytics

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'city', 'country', 'is_active']
    search_fields = ['code', 'name', 'city']

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'is_active']
    search_fields = ['code', 'name']

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ['model', 'manufacturer', 'total_seats', 'economy_seats', 'business_seats', 'first_class_seats']
    search_fields = ['model', 'manufacturer']

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'airline', 'flight_number', 'aircraft',
        'from_airport', 'to_airport', 'departure_datetime',
        'arrival_datetime', 'current_price', 'currency', 'status'
    ]
    list_filter = ['airline', 'booking_class', 'status']
    search_fields = ['flight_number', 'airline__name', 'from_airport__city', 'to_airport__city']

@admin.register(FlightSearch)
class FlightSearchAdmin(admin.ModelAdmin):
    list_display = ['search_id', 'user', 'from_airport', 'to_airport', 'departure_date', 'trip_type', 'search_timestamp']
    search_fields = ['from_airport__city', 'to_airport__city', 'user__username']

@admin.register(FlightAnalytics)
class FlightAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['flight', 'user', 'action', 'timestamp']
    search_fields = ['flight__flight_number', 'user__username']
    list_filter = ['action']
