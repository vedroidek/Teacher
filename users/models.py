from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, CustomUserManager):
    """Standard user. """
    USER_STATUS_CHOICES = [
        ('stud', 'student'),
        ('teach', 'teacher'),
        ('parent', 'parent'),
        ('oth', 'other')
    ]

    GENDER_CHOICES = [
        ('f', 'female'),
        ('m', 'male')
    ]

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    email = models.EmailField(_('email'), unique=True)
    username = models.CharField(_('username'),
                                unique=True,
                                max_length=150,
                                validators=[UnicodeUsernameValidator],
                                error_messages={'unique': _("A user with that username already exists.")},
                                help_text='At least 3 chars and no more than 150 chars')
    first_name = models.CharField(_('first_name'),
                                  max_length=150,
                                  blank=True)
    last_name = models.CharField(_('last_name'),
                                 max_length=150,
                                 blank=True)
    user_type = models.CharField(_('user_type'),
                                 choices=USER_STATUS_CHOICES,
                                 max_length=6,
                                 blank=False,
                                 null=True),
    gender = models.CharField(_('gender'),
                              max_length=1,
                              choices=GENDER_CHOICES,
                              help_text=r"'f'emale or 'm'ale",
                              blank=False, null=False)
    is_staff = models.BooleanField(_('is_admin'),
                                   default=False,
                                   editable=False)
    created_at = models.DateTimeField(_('created_at'),
                                      auto_now=True)

    objects = CustomUserManager()

    def __str__(self) -> str:
        return f'{self.username}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.username} - pk:{self.pk}'

    @property
    def full_name(self) -> str:
        if all([self.first_name, self.last_name]):
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.username}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users list"
        ordering = ['username', 'email']
        db_table = 'users'
