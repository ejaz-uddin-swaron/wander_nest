from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid

class Airport(models.Model):
    code = models.CharField(max_length=10, primary_key=True)  
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    timezone = models.CharField(max_length=50, default='Asia/Dhaka')  # Added timezone
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # For maps
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # For maps
    is_active = models.BooleanField(default=True)  # To disable airports if needed
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        ordering = ['city', 'name']

class Airline(models.Model):
    """Separate airline model for better data organization"""
    code = models.CharField(max_length=10, primary_key=True)  # e.g., BG, US
    name = models.CharField(max_length=100)  # e.g., Biman Bangladesh Airlines
    logo = models.URLField(blank=True, null=True)  # Airline logo URL
    website = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class Aircraft(models.Model):
    """Aircraft model for better aircraft management"""
    model = models.CharField(max_length=50, primary_key=True)  # e.g., Boeing 737-800
    manufacturer = models.CharField(max_length=50)  # e.g., Boeing, Airbus
    total_seats = models.PositiveIntegerField()
    economy_seats = models.PositiveIntegerField()
    business_seats = models.PositiveIntegerField(default=0)
    first_class_seats = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.model

class Flight(models.Model):
    BOOKING_CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first', 'First Class')
    ]
    
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('delayed', 'Delayed'),
        ('cancelled', 'Cancelled'),
        ('boarding', 'Boarding'),
        ('departed', 'Departed'),
        ('arrived', 'Arrived')
    ]

    id = models.CharField(max_length=50, primary_key=True)  # e.g., flight_12345
    
    # Use ForeignKey to Airline model instead of CharField
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=20)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    
    from_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    to_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    duration = models.CharField(max_length=20)
    
    # Seat management
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)
    
    # Amenities
    baggage_allowance = models.CharField(max_length=50)
    meal_included = models.BooleanField(default=False)
    wifi_available = models.BooleanField(default=False)
    entertainment_available = models.BooleanField(default=False)
    power_outlet_available = models.BooleanField(default=False)
    
    # Pricing
    booking_class = models.CharField(max_length=20, choices=BOOKING_CLASS_CHOICES)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)  # Dynamic pricing
    currency = models.CharField(max_length=10, default='BDT')
    
    # Policies
    cancellation_policy = models.TextField()
    refund_policy = models.TextField(blank=True)
    
    # Status and metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    gate = models.CharField(max_length=10, blank=True, null=True)
    terminal = models.CharField(max_length=10, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Search optimization
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)  # For promoted flights

    def __str__(self):
        return f"{self.airline.name} {self.flight_number}"
    
    @property
    def is_available(self):
        """Check if flight has available seats"""
        return self.available_seats > 0 and self.status == 'scheduled'
    
    @property
    def occupancy_rate(self):
        """Calculate occupancy percentage"""
        if self.total_seats > 0:
            return (self.booked_seats / self.total_seats) * 100
        return 0
    
    def update_available_seats(self):
        """Update available seats based on bookings"""
        self.available_seats = self.total_seats - self.booked_seats
        self.save()

    class Meta:
        ordering = ['departure_datetime']
        indexes = [
            models.Index(fields=['from_airport', 'to_airport', 'departure_datetime']),
            models.Index(fields=['departure_datetime']),
            models.Index(fields=['status']),
        ]

class Flight(models.Model):
    BOOKING_CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first', 'First Class')
    ]
    
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('delayed', 'Delayed'),
        ('cancelled', 'Cancelled'),
        ('boarding', 'Boarding'),
        ('departed', 'Departed'),
        ('arrived', 'Arrived')
    ]

    id = models.CharField(max_length=50, primary_key=True)  # e.g., flight_12345
    
    # Use ForeignKey to Airline model instead of CharField
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.CharField(max_length=20)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    
    from_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    to_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    duration = models.CharField(max_length=20)
    
    # Seat management
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)
    
    # Amenities
    baggage_allowance = models.CharField(max_length=50)
    meal_included = models.BooleanField(default=False)
    wifi_available = models.BooleanField(default=False)
    entertainment_available = models.BooleanField(default=False)
    power_outlet_available = models.BooleanField(default=False)
    
    # Pricing
    booking_class = models.CharField(max_length=20, choices=BOOKING_CLASS_CHOICES)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)  # Dynamic pricing
    currency = models.CharField(max_length=10, default='BDT')
    
    # Policies
    cancellation_policy = models.TextField()
    refund_policy = models.TextField(blank=True)
    
    # Status and metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    gate = models.CharField(max_length=10, blank=True, null=True)
    terminal = models.CharField(max_length=10, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Search optimization
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)  # For promoted flights

    def __str__(self):
        return f"{self.airline.name} {self.flight_number}"
    
    @property
    def is_available(self):
        """Check if flight has available seats"""
        return self.available_seats > 0 and self.status == 'scheduled'
    
    @property
    def occupancy_rate(self):
        """Calculate occupancy percentage"""
        if self.total_seats > 0:
            return (self.booked_seats / self.total_seats) * 100
        return 0
    
    def update_available_seats(self):
        """Update available seats based on bookings"""
        self.available_seats = self.total_seats - self.booked_seats
        self.save()

    class Meta:
        ordering = ['departure_datetime']
        indexes = [
            models.Index(fields=['from_airport', 'to_airport', 'departure_datetime']),
            models.Index(fields=['departure_datetime']),
            models.Index(fields=['status']),
        ]

class FlightSearch(models.Model):
    """Track flight searches for analytics"""
    search_id = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    from_airport = models.ForeignKey(Airport, related_name='search_departures', on_delete=models.CASCADE)
    to_airport = models.ForeignKey(Airport, related_name='search_arrivals', on_delete=models.CASCADE)
    departure_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    passengers = models.PositiveIntegerField(default=1)
    booking_class = models.CharField(max_length=20, default='economy')
    trip_type = models.CharField(max_length=20, choices=[('one_way', 'One Way'), ('round_trip', 'Round Trip')])
    
    results_count = models.PositiveIntegerField(default=0)
    search_timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Search: {self.from_airport.code} → {self.to_airport.code} on {self.departure_date}"

class FlightAnalytics(models.Model):
    """Track flight interactions for analytics"""
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    search = models.ForeignKey(FlightSearch, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=20, choices=[
        ('view', 'View'),
        ('click', 'Click'),
        ('book', 'Book')
    ])
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['flight', 'action', 'timestamp']),
        ]
