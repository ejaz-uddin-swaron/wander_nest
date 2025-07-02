from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image_url = models.URLField()
    rating = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    tags = models.JSONField()  

    def __str__(self):
        return self.name
