from django.urls import path

from world_traveller.profiles.views import profile_details

urlpatterns = [
    path('', profile_details, name='profile details'),
]

import world_traveller.profiles.signals

