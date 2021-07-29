from django.contrib import admin

from world_traveller.places.models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'description', 'likes_count',]

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Place, PlaceAdmin)
