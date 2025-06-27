from django.views.generic import TemplateView

class FlightsMapView(TemplateView):
    template_name = "flights/map.html"
