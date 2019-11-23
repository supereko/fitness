from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
        regex=r'^\+?7?\d{10}$',
        message="Номер телефона должен быть в формате +79998887766")


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
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    def __str__(self):
        return f'{ self.last_name } { self.first_name }'
