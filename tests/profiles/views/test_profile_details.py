from django.urls import reverse

from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class ProfileDetailsTest(WorldTravellerTestCase):
    def test_getProfileDetails_whenLoggedInUserWithNoPlaces_expectToGetDetailsWithNoPlaces(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(response.status_code, 200)
        self.assertListEmpty(list(response.context['places']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

        self.assertTemplateUsed(response, template_name='profiles/profile_details.html')

    def test_getProfileDetails_whenLoggedInUserWithPlaces_expectToGetDetailsWithPlaces(self):
        self.client.force_login(self.user)

        place = Place.objects.create(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/test_image.jpg',
            user=self.user,
        )

        response = self.client.get(reverse('profile details'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.id, response.context['profile'].user_id)

        self.assertListEqual([place], list(response.context['places']))
        self.assertTemplateUsed(response, template_name='profiles/profile_details.html')
