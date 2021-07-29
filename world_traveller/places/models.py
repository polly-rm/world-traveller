from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

UserModel = get_user_model()


class Place(models.Model):
    name = models.CharField(
        max_length=50,
    )

    location = models.CharField(
        max_length=50,
    )

    description = models.TextField()
    image = models.ImageField(
        upload_to='places',
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Images(models.Model):
    place = models.ForeignKey(Place, on_delete=CASCADE)
    image = models.ImageField(
        upload_to='places',
        verbose_name='Image',
        blank=True,
        null=True,
    )

