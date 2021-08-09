from django.urls import reverse

from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class PlacesListTest(WorldTravellerTestCase):
    def test_getPlacesList__whenNoPlaces_expectToListNoPlaces(self):
        response = self.client.get(reverse('list places'))

        self.assertEqual(response.status_code, 200)
        self.assertListEmpty(list(response.context['places']))
        self.assertTemplateUsed(response, template_name='places/places_list.html')

    def test_getPlacesList__whenPlaces_expectToListAllPlaces(self):
        place = Place.objects.create(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('list places'))

        self.assertEqual(response.status_code, 200)
        self.assertListEqual([place], list(response.context['places']))
        self.assertTemplateUsed(response, template_name='places/places_list.html')


