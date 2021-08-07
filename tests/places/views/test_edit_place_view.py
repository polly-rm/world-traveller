from django.urls import reverse

from tests.base.mixins import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class EditPlaceTest(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_editPlace__whenDeletePlace_expectToSucceed(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(reverse('edit place', args=(place.id,)), follow=True)
        self.assertEqual(200, response.status_code)