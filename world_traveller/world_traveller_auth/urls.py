from django.urls import path

from world_traveller.world_traveller_auth.views import SignUpView, SignInView, SignOutView

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign up'),
    path('sign_in/', SignInView.as_view(), name='sign in'),
    path('sign_out/', SignOutView.as_view(), name='sign out'),
]