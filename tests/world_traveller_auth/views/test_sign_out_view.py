from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.tests import WorldTravellerTestCase

UserModel = get_user_model()


class SignOutTests(WorldTravellerTestCase):
    def test_getSignOutView__whenGetSignOutView_expectToSucceed(self):
        response = self.client.get(reverse('sign out'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, template_name='world_traveller_auth/sign_out.html')

    def test_postSignOutView__whenSignOut_expectToSucceedAndRedirect(self):
        response = self.client.post(reverse('sign out'))
        self.assertEqual(302, response.status_code)