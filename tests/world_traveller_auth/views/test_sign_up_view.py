from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.tests import WorldTravellerTestCase

UserModel = get_user_model()


class SignUpTests(WorldTravellerTestCase):
    def test_getSignupView__whenGetSignupView_expectToSucceed(self):
        response = self.client.get(reverse('sign up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='world_traveller_auth/sign_up.html')

    def test_postSignupView__whenSignup_expectToSucceed(self):
        response = self.client.post(reverse('sign up'))
        self.assertEqual(response.status_code, 200)







