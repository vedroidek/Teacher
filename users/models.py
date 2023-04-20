from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from .manager import UserManager


class User(AbstractUser):
    """Standard user. """
    USER_STATUS_CHOICES: tuple = (
        ('stud', 'student'),
        ('teach', 'teacher'),
        ('parent', 'parent'),
        ('oth', 'other'),
    )
    REQUIRED_FIELDS = []
    objects = UserManager()
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email'), unique=True)
    status = models.CharField(_('user_type'),
                              choices=USER_STATUS_CHOICES,
                              max_length=6),
    username = models.CharField(_('username'),
                                max_length=50,
                                error_messages={'unique': _("A user with that username already exists.")},
                                help_text='No more than 50 characters')
    username_validator = UnicodeUsernameValidator()

    def __str__(self) -> str:
        return f'{self.first_name}, id = {self.pk}'

    def __repr__(self) -> str:
        return f'{super.__name__}'

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users list"
        ordering = ('email',)
