from django.urls import path

from world_traveller.places.views import place_details, like_place, comment_place, \
    edit_place, delete_place, PlacesListView, show_map, PlaceCreateView

urlpatterns = [
    path('', PlacesListView.as_view(), name='list places'),
    path('details/<int:pk>', place_details, name='place details'),
    path('like/<int:pk>', like_place, name='like place'),
    path('comment/<int:pk>', comment_place, name='comment place'),
    path('create/', PlaceCreateView.as_view(), name='create place'),
    path('edit/<int:pk>', edit_place, name='edit place'),
    path('delete/<int:pk>', delete_place, name='delete place'),

    path('map/', show_map, name='show map')
]