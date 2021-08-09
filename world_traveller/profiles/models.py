from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

'''
ProfileModel is created with built-in validators.
A property that show how much percentage a user's
profile is completed.
'''


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    is_complete = models.BooleanField(
        default=False,
    )

    @property
    def percentage_complete(self):
        percent = {'first_name': 25, 'last_name': 25, 'age': 25, 'about_me': 25,}
        total = 0
        if self.first_name:
            total += percent['first_name']
        if self.last_name:
            total += percent['last_name']
        if self.age:
            total += percent['age']
        if self.about_me:
            total += percent['about_me']

        return f"Your profile is {total}% completed"
