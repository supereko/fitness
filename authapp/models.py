from django.db import models
from django.contrib.auth.models import AbstractUser


class FitnessUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        null=True, blank=True
    )
    date_birth = models.DateField(
        verbose_name='дата рождения',
        null=True, blank=True
    )
    height = models.PositiveSmallIntegerField(
        verbose_name=' рост',
        null=True, blank=True
    )

    def __str__(self):
        return f'{ self.last_name } { self.first_name }'
