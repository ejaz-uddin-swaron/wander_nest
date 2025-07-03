from rest_framework import serializers
from flights.models import Airport, Airline, Aircraft, Flight, FlightSearch, FlightAnalytics
from bookings.models import Passenger, Booking, BookingPassenger, Payment
import uuid

### FLIGHTS SERIALIZERS ###

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    aircraft = AircraftSerializer()
    from_airport = AirportSerializer()
    to_airport = AirportSerializer()

    class Meta:
        model = Flight
        fields = '__all__'


class FlightSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightSearch
        fields = '__all__'


class FlightAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightAnalytics
        fields = '__all__'
