from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', verbose_name='Аватар', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
