from django import forms

from world_traveller.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'is_complete')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'style': 'height: 25px; width: 200px;',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'style': 'height: 25px; width: 200px;',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'style': 'height: 25px; width: 200px;',
                }
            ),
            'about_me': forms.TextInput(
                attrs={
                    'style': 'height: 60px; width: 200px;',
                }
            ),
        }
