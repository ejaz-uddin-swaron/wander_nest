from rest_framework import generics, permissions
from .models import Trip
from .serializers import TripSerializer

class UserTripListView(generics.ListAPIView):
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status_param = self.request.query_params.get('status')

        qs = Trip.objects.filter(user=user)
        if status_param in ['upcoming', 'past', 'cancelled']:
            qs = qs.filter(status=status_param)
        return qs.order_by('-start_date')
