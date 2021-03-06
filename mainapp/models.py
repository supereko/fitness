from random import random
import datetime as dt
from django.utils.timezone import now
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Extract

from authapp.models import FitnessUser 

class Photo(models.Model):
    """ Фото для галереи с автоматическим временем добавления """
    image = models.ImageField(
        upload_to='gallery', 
        null=True, blank=True
        )
    add_datetime = models.DateTimeField(
        verbose_name='время фото',
        auto_now=True
        )

    def __str__(self):
        return self.image.name


class Antropometry(models.Model):
    """ Модель для хранения антропометричесих данных
    по каждому тренирующемуся в определнный момент времени"""
    weight = models.PositiveSmallIntegerField(
        verbose_name=' вес, кг',
        #null=True, blank=True,
        )
    chest = models.PositiveSmallIntegerField(
        verbose_name=' окружность грудной клетки, см',
        #null=True, blank=True,
        )
    abdominal = models.PositiveSmallIntegerField(
        verbose_name=' окружность живота, см',
        #null=True, blank=True,
        )
    biceps = models.PositiveSmallIntegerField(
        verbose_name=' окружность бицепса, см',
        #null=True, blank=True,
        )
    thigh = models.PositiveSmallIntegerField(
        verbose_name=' окружность бедра, см',
        #null=True, blank=True,
        )
    shin = models.PositiveSmallIntegerField(
        verbose_name=' окружность голени, см',
        #null=True, blank=True,
        )
    add_datetime = models.DateTimeField(
        verbose_name='время добавления данных, см',
        #null=True, blank=True,
        )
    fitnessuser = models.ForeignKey(
        FitnessUser, 
        verbose_name = "Ссылка на тренирующегося",
        on_delete=models.CASCADE, 
        #null=True, blank=True
        )
    
    def get_effect(self):
        """ Функция расчета прогресса у тренирующегося"""
        return random.randint(1,10)


class Training(models.Model):
    """ Модель для описания тренировок """
    desc = models.TextField(
        verbose_name="Описание тренировки",
        max_length=1000,
        null=True, blank=True,
    )
    short_desc = models.CharField(
        verbose_name="Короткое описание тренировки",
        max_length=100,
        null=True, blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='активна ли тренировка',
        default=True
    )

    def __str__(self):
        return str(self.short_desc)


class Schedule(models.Model):
    """ Модель для хранения назначенных тренером занятий
    для каждого тренирующегося"""
    date = models.DateField(
        verbose_name='дата посещения тренировки',
        null=True, blank=True
        )
    time = models.TimeField(
        verbose_name='время посещения тренировки',
        null=True, blank=True
    )
    is_visit = models.BooleanField(
        verbose_name='пришел ли на тренировку',
        default=False
        )
    fitnessuser = models.ForeignKey(
        FitnessUser, 
        verbose_name="Ссылка на тренирующегося",
        on_delete=models.CASCADE, 
        null=True, blank=True
        )
    training = models.ForeignKey(
        Training,
        verbose_name="Ссылка на вид тренировки",
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.fitnessuser } { self.date } { self.time } { self.training }'

    def clean(self):
        OPEN, CLOSE = settings.OPENING_HOURS
        print(self.date, now().date())
        if self.date < now().date():
            raise ValidationError('Нельзя запланировать тренировку в прошлом')
        if self.time < dt.time(OPEN) or self.time > dt.time(CLOSE):
            raise ValidationError('Вы указали нерабочее время')


class Message(models.Model):
    """ Модель сообщений для тренера"""
    body = models.TextField(
        verbose_name='Тело сообщения',
        null=True, blank=True,
        max_length=250
    )
    fitnessuser = models.ForeignKey(
        FitnessUser,
        verbose_name="Ссылка на тренирующегося",
        on_delete=models.CASCADE,
        null=True, blank=True
        )
    timestamp = models.DateTimeField(
        verbose_name='датавремя отправки сообщения',
        null=True, blank=True,
    )

    def __str__(self):
        return self.body[:50]


@models.DateField.register_lookup
class ExtractWeek(Extract):
    """  Класс для получения номера недели в запросе с выч полем"""
    lookup_name = 'week'


@models.DateField.register_lookup
class ExtractYear(Extract):
    """  Класс для получения года в запросе с выч полем"""
    lookup_name = 'year'

