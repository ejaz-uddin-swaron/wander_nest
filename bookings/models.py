from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid
from flights.models import Flight

class Passenger(models.Model):
    TITLE_CHOICES = [
        ('mr', 'Mr'),
        ('ms', 'Ms'),
        ('mrs', 'Mrs'),
        ('dr', 'Dr'),
        ('prof', 'Prof')
    ]
    
    PASSENGER_TYPE_CHOICES = [
        ('adult', 'Adult'),
        ('child', 'Child'),
        ('infant', 'Infant')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20, blank=True)
    passport_expiry = models.DateField(null=True, blank=True)
    passenger_type = models.CharField(max_length=10, choices=PASSENGER_TYPE_CHOICES, default='adult')
    
    # Preferences
    seat_preference = models.CharField(max_length=20, choices=[
        ('window', 'Window'),
        ('aisle', 'Aisle'),
        ('middle', 'Middle')
    ], blank=True)
    meal_preference = models.CharField(max_length=20, choices=[
        ('vegetarian', 'Vegetarian'),
        ('non_vegetarian', 'Non-Vegetarian'),
        ('halal', 'Halal'),
        ('kosher', 'Kosher'),
        ('vegan', 'Vegan')
    ], blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('refunded', 'Refunded')
    ]

    booking_id = models.CharField(max_length=50, primary_key=True)
    confirmation_code = models.CharField(max_length=10, unique=True)
    pnr = models.CharField(max_length=10, unique=True)  # Passenger Name Record
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passengers = models.ManyToManyField(Passenger, through='BookingPassenger')
    
    # Contact details
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    emergency_contact_relationship = models.CharField(max_length=50, blank=True)
    
    # Booking details
    total_passengers = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='BDT')
    special_requests = models.TextField(blank=True)
    
    # Status and timestamps
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default='pending')
    booking_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    # Cancellation details
    cancelled_at = models.DateTimeField(null=True, blank=True)
    cancellation_reason = models.TextField(blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    refund_processed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Booking {self.confirmation_code} - {self.flight}"
    
    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = self.generate_confirmation_code()
        if not self.pnr:
            self.pnr = self.generate_pnr()
        super().save(*args, **kwargs)
    
    def generate_confirmation_code(self):
        """Generate unique confirmation code"""
        import random
        import string
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if not Booking.objects.filter(confirmation_code=code).exists():
                return code
    
    def generate_pnr(self):
        """Generate unique PNR"""
        import random
        import string
        while True:
            pnr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if not Booking.objects.filter(pnr=pnr).exists():
                return pnr

    class Meta:
        ordering = ['-booking_date']

class BookingPassenger(models.Model):
    """Through model for Booking-Passenger relationship"""
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10, blank=True)
    boarding_pass_url = models.URLField(blank=True)
    ticket_number = models.CharField(max_length=20, blank=True)
    ticket_url = models.URLField(blank=True)
    
    class Meta:
        unique_together = ['booking', 'passenger']

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded')
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit/Debit Card'),
        ('mobile_banking', 'Mobile Banking'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash')
    ]

    payment_id = models.CharField(max_length=50, primary_key=True)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='BDT')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    # Payment gateway details
    gateway_transaction_id = models.CharField(max_length=100, blank=True)
    gateway_response = models.JSONField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Payment {self.payment_id} - {self.amount} {self.currency}"