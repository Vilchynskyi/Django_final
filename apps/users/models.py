from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128, blank=True)
    surname = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, unique=True, db_index=True)
    phone = models.CharField(max_length=12, unique=True, db_index=True)
    telegram_id = models.CharField(max_length=25, null=True, blank=True)
    bonus = models.PositiveIntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'custom user'
        verbose_name_plural = 'custom users'

    @property
    def get_full_name(self):
        return '{} {}'.format(self.name.title(), self.surname.title())

    @property
    def get_short_name(self):
        return self.name
