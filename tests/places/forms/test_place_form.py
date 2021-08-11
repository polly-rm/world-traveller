import os

from django.core.files.uploadedfile import SimpleUploadedFile

from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.forms import PlaceForm
from world_traveller.settings import BASE_DIR


class CreatePlaceTests(WorldTravellerTestCase):
    def test_placeFormSave__whenInvalidName_expectToRaise(self):
        self.image_file = open(
            os.path.join(BASE_DIR, 'tests/media/test_image.jpg'), "rb"
        )
        data = {
            'name': 'test name',
            'location': 'Test location',
            'description': 'Test description',
        }
        files_data = {
            'image': SimpleUploadedFile(
                self.image_file.name,
                self.image_file.read()
            )
        }
        form = PlaceForm(data=data, files=files_data)

        self.assertFalse(form.is_valid())

    def test_placeFormSave__whenInvalidLocation_expectToRaise(self):
        self.image_file = open(
            os.path.join(BASE_DIR, 'tests/media/test_image.jpg'), "rb"
        )
        data = {
            'name': 'Test name',
            'location': 'test location',
            'description': 'Test description',
        }
        files_data = {
            'image': SimpleUploadedFile(
                self.image_file.name,
                self.image_file.read()
            )
        }
        form = PlaceForm(data=data, files=files_data)

        self.assertFalse(form.is_valid())

    def test_placeFormSave__whenInvalidDescription_expectToRaise(self):
        self.image_file = open(
            os.path.join(BASE_DIR, 'tests/media/test_image.jpg'), "rb"
        )
        data = {
            'name': 'Test name',
            'location': 'Test location',
            'description': 'test description',
        }
        files_data = {
            'image': SimpleUploadedFile(
                self.image_file.name,
                self.image_file.read()
            )
        }
        form = PlaceForm(data=data, files=files_data)

        self.assertFalse(form.is_valid())

    def test_placeFormSave__whenValidNameLocationDescription_expectToSucceed(self):
        self.image_file = open(
            os.path.join(BASE_DIR, 'tests/media/test_image.jpg'), "rb"
        )
        data = {
            'name': 'Test name',
            'location': 'Test location',
            'description': 'Test description',
        }
        files_data = {
            'image': SimpleUploadedFile(
                self.image_file.name,
                self.image_file.read()
            )
        }
        form = PlaceForm(data=data, files=files_data)

        self.assertTrue(form.is_valid())






