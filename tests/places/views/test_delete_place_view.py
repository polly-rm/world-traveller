from django.urls import reverse

from tests.base.utils import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class DeletePlaceTest(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_deletePlace__whenDeletePlace_expectToSucceed(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )
        self.assertListEqual(list(Place.objects.all()), [place])

        self.delete_place(place)
        self.assertListEmpty(list(Place.objects.all()))

    def test_getDeletePlaceView__whenGetDeletePlaceWithId_expectToSucceed(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('delete place', args=(place.id,)), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='places/place_delete.html')

    def test_postDeletePlaceView__whenPostDeletePlaceWithId_expectToSucceedAndRedirect(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('delete place', args=(place.id,)), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertListEmpty(list(Place.objects.all()))
        self.assertRedirects(response, '/profiles/')








