from django.core.management.base import BaseCommand
from mainapp.models import Antropometry, Training
from authapp.models import FitnessUser

import json
import os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        antropometries = load_from_json('antropometry')

        Antropometry.objects.all().delete()
        [Antropometry.objects.create(**antropometry) for antropometry in antropometries]

        trainings = load_from_json('training')
        
        Training.objects.all().delete()
        [Training.objects.create(**training) for training in trainings]


            # Создаем суперпользователя при помощи менеджера модели
        if not FitnessUser.objects.filter(username='admin').exists():
            FitnessUser.objects.create_superuser('admin', 'django@fitnes.local', '123456', date_birth='1900-01-01', height=190)