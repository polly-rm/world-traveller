from django import forms

from world_traveller.core.forms import BootstrapFormMixin
from world_traveller.profiles.models import Profile


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'style': 'height: 25px; width: 250px;',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'style': 'height: 25px; width: 250px;',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'style': 'height: 25px; width: 250px;',
                }
            ),
            'about_me': forms.TextInput(
                attrs={
                    'style': 'height: 50px; width: 250px;',
                }
            ),
        }
