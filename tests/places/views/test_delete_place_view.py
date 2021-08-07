from django.urls import reverse

from tests.base.mixins import PlaceTestUtils, UserTestUtils
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

        response = self.client.post(reverse('delete place', args=(place.id,)), follow=True)

        self.assertEqual(200, response.status_code)
        self.assertListEmpty(list(Place.objects.all()))

