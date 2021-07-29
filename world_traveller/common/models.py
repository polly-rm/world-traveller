from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

from world_traveller.places.models import Place

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )


class Like(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
