from django import forms
from world_traveller.core.mixins import BootstrapFormMixin
from world_traveller.places.models import Place, Comment


class PlaceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Place
        exclude = ('user',)


class CreatePlaceForm(PlaceForm):
    pass


class EditPlaceForm(PlaceForm):
    class Meta:
        model = Place
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                # To disable Name Field when edit a place.
                attrs={
                    'readonly': 'readonly',
                }
            )
        }


class CommentForm(forms.ModelForm):
    """
    CommentForm is created and TextField is modified
    by widgets attrs to change its size when displayed.
    """
    place_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'place_pk')

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'style': 'height: 60px; width: 1050px;',
                }
            )
        }

    def save(self, commit=True):
        place_pk = self.cleaned_data['place_pk']
        place = Place.objects.get(pk=place_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            place=place,
        )
        if commit:
            comment.save()
        return comment


