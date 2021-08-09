from django import forms
from world_traveller.core.mixins import BootstrapFormMixin
from world_traveller.profiles.models import Profile

'''
ProfileForm is created and its fields are modified
in widgets attrs so they are displayed with custom size.
Fields that do not need to be displayed are excluded.
'''


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'style': 'height: 25px; width: 250px;',
                },
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
