from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'destination', 'source', 'price', 'days')
    search_fields = ('title', 'destination', 'source')
