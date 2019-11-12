from django.urls import path

import personalapp.views as personalapp

app_name = 'personalapp'

urlpatterns = [
    path('', personalapp.index, name='index'),
    path('training/', personalapp.training, name='training'),
    path('antropometry/', personalapp.antropometry, name='antropometry'),
    path('lvlup/', personalapp.lvlup, name='lvlup'),
    path('fitnessrhomb/', personalapp.fitnessrhomb, name='fitnessrhomb'),
    path('feedback/', personalapp.feedback, name='feedback'),
]    