from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    """
    SignUp and SignIn Forms are created.
    A user signs up with an email and a password.
    """
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2',)


class SignInForm(AuthenticationForm):
    pass


# class SignInForm(forms.Form):
#     user = None
#     email = forms.EmailField()
#     password = forms.CharField(
#         widget=forms.PasswordInput(),
#     )
#
#     def clean_password(self):
#         self.user = authenticate(
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#         )
#         if not self.user:
#             raise ValidationError('Email and/or password incorrect!')
#
#     def save(self):
#         return self.user



