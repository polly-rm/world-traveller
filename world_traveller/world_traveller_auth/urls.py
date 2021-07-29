from django.urls import path

from world_traveller.world_traveller_auth.views import sign_up, sign_in, sign_out

urlpatterns = [
    path('sign_up/', sign_up, name='sign up'),
    path('sign_in/', sign_in, name='sign in'),
    path('sign_out/', sign_out, name='sign out'),
]