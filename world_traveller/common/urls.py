from django.urls import path

from world_traveller.common.views import LandingPageTemplateView, MapPageTemplateView

urlpatterns = [
    path('', LandingPageTemplateView.as_view(), name='landing page'),
    path('map/', MapPageTemplateView.as_view(), name='show map')
]