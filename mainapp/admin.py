from django.contrib import admin

from mainapp.models import Photo, Antropometry, Schedule, Training, Message
from authapp.models import FitnessUser

admin.site.register(Photo)
admin.site.register(Antropometry)
admin.site.register(Training)
admin.site.register(Schedule)
admin.site.register(Message)
admin.site.register(FitnessUser)
