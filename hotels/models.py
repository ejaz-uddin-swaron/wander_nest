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
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    type = models.CharField(max_length=20, choices=ROOM_TYPES)    
    star = models.IntegerField(default=1) 
 

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
