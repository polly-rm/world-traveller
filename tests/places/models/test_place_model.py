from django.core.exceptions import ValidationError

from tests.base.tests import WorldTravellerTestCase
from world_traveller.places.models import Place


class CreatePlaceTests(WorldTravellerTestCase):
    def test_createPlace__whenInvalidName_expectToRaise(self):
        place = Place(
            name='test name',
            location='Test location',
            description='Test description',
            image='path/to/image.png',
            user=self.user,
        )

        try:
            place.full_clean()
            place.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)
            self.assertEqual("{'name': ['This field must start with a capital letter!']}", str(ex))

    def test_createPlace__whenInvalidLocation_expectToRaise(self):
        place = Place(
            name='Test name',
            location='test location',
            description='Test description',
            image='path/to/image.png',
            user=self.user,
        )

        try:
            place.full_clean()
            place.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)
            self.assertEqual("{'location': ['This field must start with a capital letter!']}", str(ex))

    def test_createPlace__whenInvalidDescription_expectToRaise(self):
        place = Place(
            name='Test name',
            location='Test location',
            description='test description',
            image='path/to/image.png',
            user=self.user,
        )

        try:
            place.full_clean()
            place.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)
            self.assertEqual("{'description': ['This field must start with a capital letter!']}", str(ex))

    def test_createPlace__whenValidNameLocationDescription_expectToSucceed(self):
        place = Place(
            name='Test name',
            location='Test location',
            description='Test description',
            image='path/to/image.png',
            user=self.user,
        )

        place.full_clean()
        place.save()

        self.assertIsNotNone(place)
        self.assertListEqual(list(Place.objects.all()), [place])

