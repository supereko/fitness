import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('trainings/', adminapp.trainings, name='trainings'),
    path('trainings/create/', adminapp.training_create, name='training_create'),
    path('trainings/update/<int:pk>/', adminapp.training_update, name='training_update'),
    path('trainings/delete/<int:pk>/', adminapp.training_delete, name='training_delete'),

    path('schedules/', adminapp.schedules, name='schedules'),
    path('schedules/create/', adminapp.schedule_create, name='schedule_create'),
    path('schedules/update/<int:pk>/', adminapp.schedule_update, name='schedule_update'),
    path('schedules/delete/<int:pk>/', adminapp.schedule_delete, name='schedule_delete'),

    path('users/read/', adminapp.users, name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('progress/', adminapp.progress, name='progress'),
    path('messages/', adminapp.messages, name='messages'),
]
