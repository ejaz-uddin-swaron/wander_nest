import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from bookings.models import Booking, Passenger, BookingPassenger
from flights.models import Flight
from bookings.serializers import BookingSerializer, PassengerSerializer

class CreateBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        flight_id = data.get("flight_id")
        passengers_data = data.get("passengers")

        try:
            flight = Flight.objects.get(pk=flight_id)
        except Flight.DoesNotExist:
            return Response({"success": False, "error": "Flight not found"}, status=404)

        booking = Booking.objects.create(
            booking_id="booking_" + uuid.uuid4().hex[:8],
            user=user,
            flight=flight,
            total_passengers=len(passengers_data),
            contact_email=data['contact_details']['email'],
            contact_phone=data['contact_details']['phone'],
            emergency_contact_name=data['contact_details']['emergency_contact']['name'],
            emergency_contact_phone=data['contact_details']['emergency_contact']['phone'],
            emergency_contact_relationship=data['contact_details']['emergency_contact']['relationship'],
            total_amount=data['total_amount'],
            currency=data['currency'],
            special_requests=data.get('special_requests', '')
        )

        for p in passengers_data:
            passenger = Passenger.objects.create(**p)
            BookingPassenger.objects.create(booking=booking, passenger=passenger)

        serializer = BookingSerializer(booking)
        return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
