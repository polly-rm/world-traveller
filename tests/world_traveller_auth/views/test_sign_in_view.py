from django.contrib.auth import get_user_model
from django.urls import reverse
from world_traveller.world_traveller_auth.forms import SignInForm

from tests.base.tests import WorldTravellerTestCase
from tests.base.utils import PlaceTestUtils, UserTestUtils

UserModel = get_user_model()


class SignInTests(PlaceTestUtils, UserTestUtils, WorldTravellerTestCase):
    def test_getSignInView__whenGetSignInView_expectToSucceed(self):
        response = self.client.get(reverse('sign in'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='world_traveller_auth/sign_in.html')

    def test_postSignInView__whenSignIn_expectToSucceed(self):
        response = self.client.post(reverse('sign in'))

        self.assertEqual(response.status_code, 200)


