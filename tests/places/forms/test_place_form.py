from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.forms import PlaceForm


class CreatePlaceTests(WorldTravellerTestCase):
    def test_placeFormSave__whenInvalidName_expectToRaise(self):
        data = {
            'name': 'test name',
            'location': 'Test location',
            'description': 'Test description',
            'image': 'path/to/image.png',
            'user': 'self.user',
        }

        form = PlaceForm(data)
        self.assertFalse(form.is_valid())

    def test_placeFormSave__whenInvalidLocation_expectToRaise(self):
        data = {
            'name': 'Test name',
            'location': 'test location',
            'description': 'Test description',
            'image': 'path/to/image.png',
            'user': 'self.user',
        }

        form = PlaceForm(data)
        self.assertFalse(form.is_valid())

    def test_placeFormSave__whenInvalidDescription_expectToRaise(self):
        data = {
            'name': 'Test name',
            'location': 'Test location',
            'description': 'test description',
            'image': 'path/to/image.png',
            'user': 'self.user',
        }

        form = PlaceForm(data)
        self.assertFalse(form.is_valid())

    def test_placeFormSave__whenValidNameLocationDescription_expectToSucceed(self):
        data = {
            'name': 'Test name',
            'location': 'Test location',
            'description': 'Test description',
            'image': 'path/to/image.png',
            'user': 'self.user',
        }

        form = PlaceForm(data)
        self.assertTrue(form.is_valid())





