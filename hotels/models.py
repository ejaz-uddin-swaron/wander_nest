# hotels/models.py

from django.db import models

class Hotel(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('family', 'Family'),
    ]

    id = models.SlugField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 💰
    type = models.CharField(max_length=20, choices=ROOM_TYPES)     # 🏨

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
