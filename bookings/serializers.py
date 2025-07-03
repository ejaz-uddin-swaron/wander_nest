from rest_framework import serializers
from bookings.models import Passenger, Booking, BookingPassenger, Payment
from flights.serializers import FlightSerializer  

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class BookingPassengerSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer()

    class Meta:
        model = BookingPassenger
        fields = ['passenger', 'seat_number', 'boarding_pass_url', 'ticket_number', 'ticket_url']


class BookingSerializer(serializers.ModelSerializer):
    passengers = BookingPassengerSerializer(source='bookingpassenger_set', many=True, read_only=True)
    flight = FlightSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


