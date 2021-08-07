import random
from os.path import join

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from tests.base.tests import WorldTravellerTestCase
from world_traveller.profiles.models import Profile

from world_traveller.places.models import Place


class ProfileDetailsTest(WorldTravellerTestCase):
    def test_getDetails_whenLoggedInUserWithNoPlaces_shouldGetDetailsWithNoPlaces(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['places']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithPlaces_shouldGetDetailsWithPlaces(self):
        place = Place.objects.create(
            name='Test Place Name',
            location='Test Place Location',
            description='Test place description',
            image='path/to/image.png',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([place], list(response.context['places']))

    # def test_postDetails_whenUserLoggedInWithoutImage_shouldChangeImage(self):
    #     path_to_image = join(settings.BASE_DIR, 'places', 'media', 'test_profile_image.jpg')
    #
    #     file_name = f'{random.randint(1, 10000)}-test_profile_image.jpg'
    #     file = SimpleUploadedFile(
    #         name=file_name,
    #         content=open(path_to_image, 'rb').read(),
    #         content_type='image/jpg')
    #
    #     self.client.force_login(self.user)
    #
    #     response = self.client.post(reverse('profile details'), data={
    #         'profile_image': file,
    #     })
    #
    #     self.assertEqual(302, response.status_code)
    #
    #     profile = Profile.objects.get(pk=self.user.id)
    #     self.assertTrue(str(profile.profile_image).endswith(file_name))

    def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)

        # profile = Profile.objects.get(pk=self.user.id)
        # self.assertEqual(path_to_image, str(profile.profile_image))