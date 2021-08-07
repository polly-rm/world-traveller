from django.urls import reverse

from tests.base.mixins import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.forms import CreatePlaceForm
from world_traveller.places.models import Place


class CreatePlaceViewTests(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_createPlace__whenIsAuthenticated_expectToCreatePlace(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )
        self.assertListEqual(list(Place.objects.all()), [place])

        response = self.client.get(reverse('create place'))
        self.assertEqual(200, response.status_code)

    def test_createPlace__whenNotAuthenticated_expectToRedirect(self):
        response = self.client.get(reverse('create place'))
        self.assertEqual(302, response.status_code)

