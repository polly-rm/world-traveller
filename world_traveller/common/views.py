from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageTemplateView(TemplateView):
    template_name = 'landing_page.html'


def test(request):
    return render(request, 'index.html')