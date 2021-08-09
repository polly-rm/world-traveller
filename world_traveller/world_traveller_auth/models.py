from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from world_traveller.world_traveller_auth.managers import WorldTravellerUserManager

'''
Custom UserModel is created and extended.
A user uses an email to authenticate.
'''


class WorldTravellerUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    objects = WorldTravellerUserManager()

    USERNAME_FIELD = 'email'

