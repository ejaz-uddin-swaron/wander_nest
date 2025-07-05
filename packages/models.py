from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TransportOption(models.Model):
    TYPE_CHOICES = [('bus', 'Bus'), ('train', 'Train'), ('flight', 'Flight'), ('car', 'Car')]

    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    capacity = models.PositiveIntegerField()
    features = models.JSONField(default=list)  # List of strings

    def __str__(self):
        return self.name


class HotelOption(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # per night
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # 1 to 5
    location = models.CharField(max_length=255)
    amenities = models.JSONField(default=list)  # List of strings
    room_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GuideOption(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # per day
    rating = models.DecimalField(max_digits=2, decimal_places=1)  # 1 to 5
    experience_years = models.PositiveIntegerField()
    languages = models.JSONField(default=list)
    specialties = models.JSONField(default=list)

    def __str__(self):
        return self.name


class Package(models.Model):
    STATUS_CHOICES = [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    travelers_count = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    transport = models.ForeignKey(TransportOption, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(HotelOption, on_delete=models.SET_NULL, null=True, blank=True)
    guide = models.ForeignKey(GuideOption, on_delete=models.SET_NULL, null=True, blank=True)

    preferences = models.JSONField(default=dict)  # e.g., { skip_guide: true }

    def __str__(self):
        return self.title
