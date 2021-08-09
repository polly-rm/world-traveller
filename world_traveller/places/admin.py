from django.contrib import admin

from world_traveller.places.models import Place

'''
Register PlaceModel in administration.
'''


class PlaceAdmin(admin.ModelAdmin):
    # Filter the fields that need to be displayed.
    list_display = ['name', 'location', 'description', 'likes_count',]

    # To show how many likes each place has.
    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Place, PlaceAdmin)
