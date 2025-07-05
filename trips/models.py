import uuid
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Trip(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
        ('cancelled', 'Cancelled'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    duration = models.CharField(max_length=50)  # e.g. '5 days'
    activities_count = models.PositiveIntegerField(default=0)
    check_in_time = models.CharField(max_length=20)  # e.g. '3:00 PM'
    weather = models.CharField(max_length=100)  # e.g. 'Sunny, 28°C'
    currency = models.CharField(max_length=10)  # e.g. 'BDT'
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    travelers = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
