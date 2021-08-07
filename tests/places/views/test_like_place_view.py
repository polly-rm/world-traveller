from django.urls import reverse

from world_traveller.common.models import Like
from world_traveller.places.models import Place
from tests.base.mixins import UserTestUtils, PlaceTestUtils
from tests.base.tests import WorldTravellerTestCase


class LikePlaceViewTests(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_likePlace__whenPlaceNotLiked_shouldCreateLike(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='poliTest2@abv.bg', password='1234')
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('like place', kwargs={
            'pk': place.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            place_id=place.id,
        ) \
            .exists()

        self.assertTrue(like_exists)

    def test_likePlace__whenPlaceAlreadyLiked_shouldDeleteTheLike(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='poliTest2@abv.bg', password='1234')
        place = self.create_place_with_like(
            like_user=self.user,
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('like place', kwargs={
            'pk': place.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            place_id=place.id,
        ) \
            .exists()

        self.assertFalse(like_exists)