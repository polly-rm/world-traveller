from django import forms

from world_traveller.common.models import Comment
from world_traveller.places.models import Place


class CommentForm(forms.ModelForm):
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

