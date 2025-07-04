# reviews/admin.py

from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'date', 'likes', 'comments']
    search_fields = ['user__username', 'content']
    list_filter = ['rating', 'date']
