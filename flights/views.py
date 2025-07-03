from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from flights.models import Flight, Airport
from flights.serializers import FlightSerializer, AirportSerializer

class FlightSearchView(APIView):
    def post(self, request):
        data = request.data
        from_city = data.get("from")
        to_city = data.get("to")
        departure_date = data.get("departure_date")

        flights = Flight.objects.filter(
            from_airport__city__iexact=from_city,
            to_airport__city__iexact=to_city,
            departure_datetime__date=departure_date,
            status='scheduled'
        )

        serializer = FlightSerializer(flights, many=True)
        return Response({
            "success": True,
            "data": serializer.data,
            "total": len(serializer.data)
        })


class FlightDetailView(APIView):
    def get(self, request, flight_id):
        try:
            flight = Flight.objects.get(pk=flight_id)
            serializer = FlightSerializer(flight)
            return Response({"success": True, "data": serializer.data})
        except Flight.DoesNotExist:
            return Response({"success": False, "error": "Flight not found"}, status=404)


class AirportListView(APIView):
    def get(self, request):
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response({"success": True, "data": serializer.data})