from django.urls import path

from world_traveller.profiles.views import delete_profile, profile_details

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('delete/', delete_profile, name='delete profile'),
]

import world_traveller.profiles.signals

