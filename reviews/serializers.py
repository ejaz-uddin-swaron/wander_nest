# reviews/serializers.py

from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'user', 'date', 'rating', 'content', 'likes', 'comments']

    def get_user(self, obj):
        return {
            "name": obj.user.get_full_name() or obj.user.username,
            "avatar": obj.avatar or "/placeholder.svg?height=40&width=40"
        }
