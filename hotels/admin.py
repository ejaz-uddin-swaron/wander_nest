from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'price', 'type', 'star')
    search_fields = ('name', 'location')
    list_filter = ('star', 'type')
