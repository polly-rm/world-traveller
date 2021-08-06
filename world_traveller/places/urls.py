from django.urls import path

from world_traveller.places.views import PlacesListView, show_map, PlaceDetailsView, \
    CommentPlaceView, like_place, CreatePlaceView, EditPlaceView, DeletePlaceView

urlpatterns = [
    path('', PlacesListView.as_view(), name='list places'),
    path('details/<int:pk>', PlaceDetailsView.as_view(), name='place details'),
    path('like/<int:pk>', like_place, name='like place'),
    path('comment/<int:pk>', CommentPlaceView.as_view(), name='comment place'),
    path('create/', CreatePlaceView.as_view(), name='create place'),
    path('edit/<int:pk>', EditPlaceView.as_view(), name='edit place'),
    path('delete/<int:pk>', DeletePlaceView.as_view(), name='delete place'),

    path('map/', show_map, name='show map')
]