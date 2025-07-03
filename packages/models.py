from django.db import models

class Package(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    destination = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    days = models.PositiveIntegerField()

    def __str__(self):
        return self.title
