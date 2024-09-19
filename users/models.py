from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта', help_text='Введите почту')
    avatar = models.ImageField(upload_to='users/avatars', blank=True,
                               null=True, verbose_name='аватар')
    phone = models.CharField(
        max_length=35, blank=True,
        null=True, verbose_name='номер телефона', help_text='Введите номер телефона')
    country = models.CharField(max_length=100, blank=True,
                               null=True, verbose_name='страна')
    token = models.CharField(max_length=100, verbose_name='токен', blank=True,
                             null=True, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
