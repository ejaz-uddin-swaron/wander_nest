from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'rating')
    search_fields = ('name', 'location', 'cuisine')
    list_filter = ('tags',)
