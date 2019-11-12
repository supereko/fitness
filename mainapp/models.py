from random import random
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
        verbose_name=' вес',
        null=True, blank=True,
        )
    chest = models.PositiveSmallIntegerField(
        verbose_name=' окружность грудной клетки',
        null=True, blank=True,
        )
    abdominal = models.PositiveSmallIntegerField(
        verbose_name=' окружность живота',
        null=True, blank=True,
        )
    biceps = models.PositiveSmallIntegerField(
        verbose_name=' окружность бицепса',
        null=True, blank=True,
        )
    thigh = models.PositiveSmallIntegerField(
        verbose_name=' окружность бедра',
        null=True, blank=True,
        )
    shin = models.PositiveSmallIntegerField(
        verbose_name=' окружность голени',
        null=True, blank=True,
        )
    add_datetime = models.DateTimeField(
        verbose_name='время добавления данных', 
        auto_now=True
        )
    fitnessuser = models.ForeignKey(
        FitnessUser, 
        verbose_name = "Ссылка на тренирующегося",
        on_delete=models.CASCADE, 
        null=True, blank=True
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

    def __str__(self):
        return self.short_desc


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
        verbose_name='пришел ли ты на тренировку',
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


@models.DateField.register_lookup
class ExtractWeek(Extract):
    """  Класс для получения номера недели в запросе с выч полем"""
    lookup_name = 'week'


@models.DateField.register_lookup
class ExtractYear(Extract):
    """  Класс для получения года в запросе с выч полем"""
    lookup_name = 'year'

