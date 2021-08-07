from django.urls import reverse

from world_traveller.places.models import Place
from tests.base.mixins import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase


class PlaceDetailsTest(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_getPlaceDetails_whenPlaceExistsAndIsOwner_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('place details', kwargs={
            'pk': place.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPlaceDetails_whenPlaceExistsAndIsNotOwnerAndNotLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='poliTest2@abv.bg', password='1234')
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=place_user,
        )

        response = self.client.get(reverse('place details', kwargs={
            'pk': place.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_getPlaceDetails_whenPlaceExistsAndIsNotOwnerAndLiked_shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='poliTest2@abv.bg', password='1234')
        place = self.create_place_with_like(
            like_user=self.user,
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=place_user,
        )

        response = self.client.get(reverse('place details', kwargs={
            'pk': place.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])