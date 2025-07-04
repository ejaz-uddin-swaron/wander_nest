# reviews/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.URLField(blank=True)  # Optional if you want custom avatars
    date = models.DateField(auto_now_add=True)
    rating = models.PositiveIntegerField(default=5)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)  # You can replace later with FK

    def __str__(self):
        return f"{self.user.username}'s review ({self.rating}⭐)"
