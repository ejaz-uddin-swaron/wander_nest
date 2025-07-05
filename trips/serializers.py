from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id', 'title', 'start_date', 'end_date', 'location', 'status', 
            'duration', 'activities_count', 'check_in_time', 'weather', 
            'currency', 'image', 'price', 'travelers', 'created_at', 'updated_at'
        ]
