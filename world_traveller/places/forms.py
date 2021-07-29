import os
from os.path import join

from django import forms
from django.conf import settings

from world_traveller.core.forms import BootstrapFormMixin
from world_traveller.places.models import Place


class PlaceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Place
        exclude = ('user',)


class CreatePlaceForm(PlaceForm):
    pass


class EditPlaceForm(PlaceForm):
    def save(self, commit=True):
        db_place = Place.objects.get(pk=self.instance.id)
        if commit:
            os.remove(join(settings.MEDIA_ROOT, str(db_place.image)))
        return super().save()

    class Meta:
        model = Place
        fields = '__all__'
