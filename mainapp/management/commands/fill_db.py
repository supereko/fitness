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
        for antropometry in antropometries:
            new_antropometry = Antropometry(**antropometry)
            new_antropometry.save()
        
        trainings = load_from_json('training')
        
        Training.objects.all().delete()
        for training in trainings:
            new_training = Antripometry(**training)
            new_training.save()

            # Создаем суперпользователя при помощи менеджера модели
        if not User.objects.filter(username='admin').exists():
            FitnessUser.objects.create_superuser('admin', 'django@fitnes.local', '123456', date_birth=1900-01-01, height=190)