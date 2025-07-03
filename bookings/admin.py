from django.contrib import admin
from .models import Passenger, Booking, BookingPassenger, Payment

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'passport_number', 'nationality']
    search_fields = ['first_name', 'last_name', 'passport_number', 'email']
    list_filter = ['passenger_type', 'nationality']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'confirmation_code', 'user', 'flight', 'status', 'booking_date', 'total_amount', 'currency']
    search_fields = ['booking_id', 'confirmation_code', 'user__username', 'flight__flight_number']
    list_filter = ['status', 'currency', 'booking_date']

@admin.register(BookingPassenger)
class BookingPassengerAdmin(admin.ModelAdmin):
    list_display = ['booking', 'passenger', 'seat_number']
    search_fields = ['booking__booking_id', 'passenger__passport_number']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'booking', 'amount', 'currency', 'payment_method', 'status', 'created_at']
    search_fields = ['payment_id', 'booking__booking_id']
    list_filter = ['status', 'payment_method', 'currency']
