from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=50, unique=True, verbose_name='почта')

    code = models.CharField(max_length=4, verbose_name='проверочный код')
    is_active = models.BooleanField(default=False, verbose_name='пользователь активен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
