from django.urls import reverse

from tests.base.utils import PlaceTestUtils, UserTestUtils
from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class CreatePlaceViewTests(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_CreatePlace__whenIsAuthenticated_expectToSucceed(self):
        self.client.force_login(self.user)
        place = self.create_place(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )
        self.assertListEqual(list(Place.objects.all()), [place])

    def test_getCreatePlaceView__whenIsAuthenticated_expectToSucceed(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('create place'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='places/place_create.html')

    def test_getCreatePlace__whenIsNotAuthenticated_expectNotToGetCreatePlaceViewAndRedirect(self):
        response = self.client.get(reverse('create place'))
        self.assertEqual(response.status_code, 302)

    def test_postCreatePlaceView__whenIsAuthenticated_expectToSucceed(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('create place'))

        self.assertEqual(response.status_code, 200)






