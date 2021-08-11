from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

from world_traveller.core.validators import validate_text_starts_with_capital

UserModel = get_user_model()

'''
PlaceModel is created with custom and built-in
fields validators. Foreign-key connection is 
created with the user that add the place.
'''


class Place(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[validate_text_starts_with_capital],
    )

    location = models.CharField(
        max_length=50,
        validators=[validate_text_starts_with_capital],
    )

    description = models.TextField(
        validators=[validate_text_starts_with_capital],
    )
    image = models.ImageField(
        upload_to='places',
    )
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


'''
CommentModel is created with foreign-key connection
to the place that it refers to. This is how users
can comment each place and comments can be displayed.
'''


class Comment(models.Model):
    text = models.TextField(
        max_length=200,
    )
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=CASCADE,
    )


'''
LikeModel is created with foreign-key connection
to the place that it refers to. This is how users
can like each place and likes number can be displayed.
'''


class Like(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


'''
ImagesModel is created with foreign-key connection
to the place that it refers to. This is how a user
can add multiple images for one place.
'''


class Images(models.Model):
    place = models.ForeignKey(Place, on_delete=CASCADE)
    image = models.ImageField(
        upload_to='places',
        verbose_name='Image',
        blank=True,
        null=True,
    )





