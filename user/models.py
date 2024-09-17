from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='Электронная почта')

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
