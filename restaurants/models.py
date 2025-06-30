from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='restaurants/')
    rating = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    tags = models.JSONField()  # Requires PostgreSQL; use TextField if using SQLite

    def __str__(self):
        return self.name
