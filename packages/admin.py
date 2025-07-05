from django.contrib import admin
from .models import (
    TransportOption,
    HotelOption,
    GuideOption,
    Package
)


@admin.register(TransportOption)
class TransportOptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price', 'capacity']
    search_fields = ['name', 'type']
    list_filter = ['type']
    ordering = ['type', 'name']


@admin.register(HotelOption)
class HotelOptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'location', 'room_type']
    search_fields = ['name', 'location']
    list_filter = ['rating', 'location']
    ordering = ['-rating']


@admin.register(GuideOption)
class GuideOptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'experience_years']
    search_fields = ['name', 'languages']
    list_filter = ['rating', 'experience_years']
    ordering = ['-rating']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'from_location', 'to_location', 'start_date', 'end_date', 'status', 'total_cost']
    search_fields = ['title', 'from_location', 'to_location', 'user__username']
    list_filter = ['status', 'start_date', 'end_date']
    readonly_fields = ['created_at', 'updated_at', 'total_cost']
    ordering = ['-created_at']

from django.contrib import admin
from .models import PreMadePackage

@admin.register(PreMadePackage)
class PreMadePackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'destination', 'price']
    search_fields = ['title', 'destination']
