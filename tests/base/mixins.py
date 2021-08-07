from django.contrib.auth import get_user_model

from world_traveller.common.models import Like, Comment
from world_traveller.places.models import Place

UserModel = get_user_model()


class PlaceTestUtils:
    def create_place(self, **kwargs):
        return Place.objects.create(**kwargs)

    def create_place_with_like(self, like_user, **kwargs):
        place = self.create_place(**kwargs)
        Like.objects.create(
            place=place,
            user=like_user,
        )
        return place

    def create_place_with_comment(self, comment_user, **kwargs):
        place = self.create_place(**kwargs)
        Comment.objects.create(
            place=place,
            user=comment_user,
        )
        return place


class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)