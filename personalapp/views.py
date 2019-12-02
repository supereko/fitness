import datetime as dt
from django.db.models import Max, Min, Sum, Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.utils.timezone import now
from django.urls import reverse
from django.forms.formsets import formset_factory
from qsstats import QuerySetStats

from mainapp.models import Schedule, ExtractWeek, Message, Antropometry
from personalapp.forms import AddAntropometryForm, AddMessageForm

@login_required
def index(request):
    today = dt.date.today()
    monday = today + dt.timedelta(days=-today.weekday())
    # получаем список дат в текущей неделе
    day_current_week = [monday + dt.timedelta(days=i) for i in range(7)]
    # получаем список часов работы тренажерного зала с 7:00 до 22:00
    hour_current_day = [dt.time(7 + i) for i in range(16)]
    week_number = now().isocalendar()[1]
    shed_user = Schedule.objects.filter(
        fitnessuser=request.user
        )
    future_shed_user = shed_user.filter(date__gt=now())
    items = shed_user.annotate(
        week=ExtractWeek('date')).filter(
        week=week_number
    )
    context = {
        'future_shed_user': future_shed_user,
        'items': items,
        'day_with_shedul': items.values_list('date', flat=True),
        'time_with_shedul': items.values_list('time', flat=True),
        'day_current_week': day_current_week,
        'hour_current_day': hour_current_day,
        'now': now()
    }
    return render(request, 'personalapp/index.html', context)


def training(request):
    context = {}
    return render(request, 'personalapp/training.html', context)

@login_required
def antropometry(request):
    """ Функция для добавления промежуточных антропометрических данных"""
    if request.method == 'POST':
        form = AddAntropometryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('personal:index'))
    else:
        form = AddAntropometryForm(initial={'fitnessuser': request.user,
                                            'add_datetime': now()
                                            })

    antropometries = Antropometry.objects.filter(fitnessuser=request.user)

    context = {
        'title': 'Новые антропометрические данные',
        'form': form,
        'antropometries': antropometries,
    }
    return render(request, 'personalapp/antropometry.html', context)


def lvlup(request):
    user_ant = Antropometry.objects.filter(fitnessuser=request.user).all()
    start_date = user_ant.aggregate(
        Min('add_datetime'))['add_datetime__min']
    end_date = user_ant.aggregate(
        Max('add_datetime'))['add_datetime__max']

    qsstats = QuerySetStats(user_ant, date_field='add_datetime', aggregate=Max('weight'))
    pre_values = qsstats.time_series(start_date, end_date, interval='days')
    # Список данных, где нулевые значения замненены на предыдущие
    # ненулевые, чтобы не было провалов на графике
    values = []
    for_next_zero = 50 # будет выведено, если в наборе весов самым ранним значением 0
    for item in pre_values:
        if item[1]:
            values.append((item[0], item[1]))
            for_next_zero = item[1]
        else:
            values.append((item[0], for_next_zero))
    return render(request, 'personalapp/lvlup.html', {'values': values})


def fitnessrhomb(request):
    context = {}
    return render(request, 'personalapp/fitnessrhomb.html', context)


def feedback(request):
    """ Функция для отправки сообщения админу """
    if request.method == 'POST':
        form = AddMessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('personal:index'))
    else:
        if request.user.is_authenticated:
            form = AddMessageForm(initial={'fitnessuser': request.user,
                                           'timestamp': now()
                                           })
        else:
            return HttpResponseRedirect(reverse('auth:login'))

    context = {
        'title': 'Новое сообщение',
        'form': form
    }
    return render(request, 'personalapp/feedback.html', context)
