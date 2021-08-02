from django.urls import path

from world_traveller.profiles.views import profile_details, delete_profile

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('delete/', delete_profile, name='delete profile'),
]

import world_traveller.profiles.signals

