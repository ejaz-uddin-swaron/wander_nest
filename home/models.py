from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='hero/')

class FeatureDestination(models.Model):
    pic = models.ImageField(upload_to='destinations/')
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OurService(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
