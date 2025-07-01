from django.contrib import admin
from .models import HeroSection, FeatureDestination, OurService, Destination

@admin.register(HeroSection)
class HomeHeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')  
    search_fields = ('title',)

@admin.register(FeatureDestination)
class FeaturedDestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle') 
    search_fields = ('title',)

@admin.register(OurService)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')  
    search_fields = ('title',)

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'click') 
    search_fields = ('name',)
    readonly_fields = ('click',)
