from django.views.generic import TemplateView


class LandingPageTemplateView(TemplateView):
    template_name = 'landing_page.html'


# TODO: Map Geocoder to take a place address and redirect to it.
class MapPageTemplateView(TemplateView):
    template_name = 'map.html'
