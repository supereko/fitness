import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('trainings/', adminapp.trainings, name='trainings'),
    path('trainings/create/', adminapp.training_create, name='training_create'),
    path('trainings/update/<int:pk>/', adminapp.training_update, name='training_update'),
    path('trainings/delete/<int:pk>/', adminapp.training_delete, name='training_delete'),

    path('scedules/', adminapp.scedules, name='scedules'),
    path('scedules/create/', adminapp.scedule_create, name='scedule_create'),
    path('scedules/update/<int:pk>/', adminapp.scedule_update, name='scedule_update'),
    path('scedules/delete/<int:pk>/', adminapp.scedule_delete, name='scedule_delete'),

    path('users/read/', adminapp.users, name='users'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('progress/', adminapp.progress, name='progress'),
    path('messages/', adminapp.messages, name='feedback'),
]
