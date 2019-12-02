from django.db.models import Max
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import Photo, Antropometry


def gallery(request):
    photo_list = Photo.objects.order_by('add_datetime')
    paginator = Paginator(photo_list, 8)
    page = request.GET.get('page', 1)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {
        'title': 'Галерея фото',
        'photos': photos,
    }
    return render(request, 'mainapp/gallery.html', context)


def exercise(request):
    return render(request, 'mainapp/exercise.html', {'title': 'техника упражнений'})


def diet(request):
    return render(request, 'mainapp/diet.html', {'title': 'питание'})


def progress(request):
    max_abdominal = Antropometry.objects.aggregate(Max('abdominal'))
    winner = Antropometry.objects.filter(abdominal=max_abdominal).first()
    context = {
        'title': 'прогресс месяца',
        'winner': winner,
    }
    return render(request, 'mainapp/progress.html', context)
