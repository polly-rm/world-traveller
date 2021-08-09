from django.urls import reverse

from tests.base.utils import UserTestUtils, PlaceTestUtils
from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Like


class LikePlaceViewTests(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_likePlace__whenPlaceNotLiked_expectToCreateLike(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='email_test2', password='password_test2')

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

        self.assertEqual(response.status_code, 302)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            place_id=place.id,
        ) \
            .exists()

        self.assertTrue(like_exists)

    def test_likePlace__whenPlaceAlreadyLiked_expectToDeleteTheLike(self):
        self.client.force_login(self.user)
        place_user = self.create_user(email='email_test2', password='password_test2')

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

        self.assertEqual(response.status_code, 302)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            place_id=place.id,
        ) \
            .exists()

        self.assertFalse(like_exists)