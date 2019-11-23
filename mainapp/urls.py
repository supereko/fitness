from django.urls import path
from django.contrib import admin

import mainapp.views as mainapp

app_name = 'main'

urlpatterns = [
    path('', mainapp.gallery, name='index'),
    path('gallery/', mainapp.gallery, name='gallery'),
    path('exercise/', mainapp.exercise, name='exercise'),
    path('diet/', mainapp.diet, name='diet'),
    path('progress/', mainapp.progress, name='progress'),
]