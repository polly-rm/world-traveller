from django.urls import reverse

from tests.base.utils import PlaceTestUtils, UserTestUtils
from world_traveller.profiles.models import Profile, UserModel

from tests.base.tests import WorldTravellerTestCase


class ProfileDeleteTest(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_deleteProfile_whenDeleteLoggedInUserProfile_expectToDeleteProfileAndItsUser(self):
        self.client.force_login(self.user)
        profile = Profile.objects.get(pk=self.user.id)
        profile.user.delete()

        self.assertListEmpty(list(UserModel.objects.all()))
        self.assertListEmpty(list(Profile.objects.all()))

    def test_getDeleteProfileView__whenGetDeleteProfileView_expectToSucceed(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='profiles/profile_delete.html')

    def test_postDeleteProfileView__whenPostProfileView_expectToSucceedAndRedirect(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete profile'))

        self.assertEqual(response.status_code, 302)
        self.assertListEmpty(list(UserModel.objects.all()))
        self.assertListEmpty(list(Profile.objects.all()))





