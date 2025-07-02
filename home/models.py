from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    image_url = models.URLField()

class FeatureDestination(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    large_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()
    description = models.TextField()
    large_description = models.TextField()
    click = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class OurService(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
