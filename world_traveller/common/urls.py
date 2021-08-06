from django.urls import path

from world_traveller.common.views import test, LandingPageTemplateView


urlpatterns = [
    path('', LandingPageTemplateView.as_view(), name='landing page'),
    path('test/', test),
]