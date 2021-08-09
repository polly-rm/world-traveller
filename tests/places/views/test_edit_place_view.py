from django.urls import reverse

from tests.base.utils import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase


class EditPlaceTest(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_EditPlace__whenGetEditPlaceViewWithId_expectToSucceed(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('edit place', args=(place.id,)), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='places/place_edit.html')

    def test_editPlace__whenEditPlaceWithId_expectToSucceedAndRedirect(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.post(
            reverse('edit place', kwargs={'pk': place.id}),
            {'name': 'Test Place Name2', 'location': 'Test Place Location2', 'description': 'Test place description',})

        self.assertEqual(response.status_code, 302)

        place.refresh_from_db()
        self.assertEqual(place.name, 'Test Place Name2')
        self.assertEqual(place.location, 'Test Place Location2')

        self.assertRedirects(response, '/profiles/')



