import datetime as dt
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.utils.timezone import now

from mainapp.models import Schedule, ExtractWeek
from personalapp.forms import AddAntropometryForm


def index(request):
    today = dt.date.today()
    monday = today + dt.timedelta(days=-today.weekday())
    # получаем список дат в текущей неделе
    day_current_week = [monday + dt.timedelta(days=i) for i in range(7)]
    # получаем список часов работы тренажерного зала с 7:00 до 22:00
    hour_current_day = [dt.time(7 + i) for i in range(16)]
    week_number = now().isocalendar()[1]
    items = Schedule.objects.annotate(
        week=ExtractWeek('date')).filter(
        week=week_number
    )
    if not request.user.is_superuser:
        items = items.filter(
        fitnessuser=request.user
        )
    context = {
        'items': items,
        'day_with_shedul': items.values_list('date', flat=True),
        'time_with_shedul': items.values_list('time', flat=True),
        'day_current_week': day_current_week,
        'hour_current_day': hour_current_day,
    }
    return render(request, 'personalapp/index.html', context)


def training(request):
    context = {}
    return render(request, 'personalapp/training.html', context)


def antropometry(request):
    form = AddAntropometryForm()
    context = {
        'form': form
    }
    return render(request, 'personalapp/antropometry.html', context)


def lvlup(request):
    context = {}
    return render(request, 'personalapp/lvlup.html', context)


def fitnessrhomb(request):
    context = {}
    return render(request, 'personalapp/fitnessrhomb.html', context)


def feedback(request):
    context = {}
    return render(request, 'personalapp/feedback.html', context)