from django.urls import reverse

from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class PlacesListTest(WorldTravellerTestCase):
    def test_getPlacesList__whenNoPlaces_shouldListNoPlaces(self):
        response = self.client.get(reverse('list places'))
        self.assertEqual(200, response.status_code)
        self.assertListEmpty(list(response.context['places']))

    def test_getPlacesList__whenPlaces_shouldListAllPlaces(self):
        place = Place.objects.create(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('list places'))

        self.assertEqual(200, response.status_code)
        self.assertListEqual([place], list(response.context['places']))


