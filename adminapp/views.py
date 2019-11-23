from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now

from authapp.forms import FitnessUserRegisterForm
from adminapp.forms import (FitnessUserAdminEditForm,
                            TrainingCreateForm, TrainingEditForm,
                            ScheduleCreateForm, ScheduleEditForm)
from mainapp.models import (FitnessUser, ExtractYear, Training,
                            Schedule, Message)


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    year = now().isocalendar()[0]
    users_list = FitnessUser.objects.annotate(
        age=year-ExtractYear('date_birth')).order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username'
    )
    paginator = Paginator(users_list, 3)
    page = request.GET.get('page', 1)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'title': 'админка/пользователи',
        'users': users,
        }

    return render(request, 'adminapp/users.html', context)


def user_create(request):

    if request.method == 'POST':
        form = FitnessUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = FitnessUserRegisterForm()
    
    context = {
        'title': 'пользователи/создание', 
        'update_form': form
        }
    
    return render(request, 'adminapp/user_update.html', context)


def user_update(request, pk):

    edit_user = get_object_or_404(FitnessUser, pk=pk)
    if request.method == 'POST':
        edit_form = FitnessUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update',\
                                                args=[edit_user.pk]))
    else:
        edit_form = FitnessUserAdminEditForm(instance=edit_user)
    
    context = {
        'title': 'пользователи/редактирование', 
        'update_form': edit_form
        }
    return render(request, 'adminapp/user_update.html', context)



def user_delete(request, pk):
    user = get_object_or_404(FitnessUser, pk=pk)
    
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    context = {
        'title': 'пользователи/удаление', 
        'user_to_delete': user
        }
    
    return render(request, 'adminapp/user_delete.html', context)


def trainings(request):
    """ Функция для отображения тренировок """
    trainings = Training.objects.filter(is_active=True).all()
    context = {
        'trainings': trainings,
    }
    return render(request, 'adminapp/trainings.html', context)


def training_create(request):
    """ Функция для отображения формы создания новой тренировки"""
    if request.method == 'POST':
        form = TrainingCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = TrainingCreateForm()

    context = {
        'title': 'тренировки/создание',
        'form': form
    }
    return render(request, 'adminapp/training_create.html', context)


def training_update(request, pk):
    """ Функция для отображения формы редактирования новой тренировки"""
    edit_training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        form = TrainingEditForm(request.POST, request.FILES, instance=edit_training)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:training_update', \
                                                args=[edit_training.pk]))
    else:
        form = TrainingEditForm(instance=edit_training)

    context = {
        'title': 'Тренировки/редактирование',
        'form': form
    }
    return render(request, 'adminapp/training_create.html', context)


def training_delete(request, pk):
    """ Функция для отображения формы удаления новой тренировки """
    training = get_object_or_404(Training, pk=pk)

    if request.method == 'POST':
        training.is_active = False
        training.save()
        return HttpResponseRedirect(reverse('admin:trainings'))

    context = {
        'title': 'тренировки/удаление',
        'training_to_delete': training
    }

    return render(request, 'adminapp/training_delete.html', context)


def schedules(request):
    """ Функция для отображения занятий """
    schedules = Schedule.objects.all()
    context = {
        'schedules': schedules,
    }
    return render(request, 'adminapp/schedules.html', context)


def schedule_create(request):
    """ Функция для отображения формы создания нового занятия"""
    if request.method == 'POST':
        form = ScheduleCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:schedules'))
    else:
        form = ScheduleCreateForm()

    context = {
        'title': 'занятие/создание',
        'form': form
    }
    return render(request, 'adminapp/schedule_create.html', context)


def schedule_update(request, pk):
    """ Функция для отображения формы редактирования нового занятия"""
    edit_schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleEditForm(request.POST, request.FILES, instance=edit_schedule)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:schedule_update', \
                                                args=[edit_schedule.pk]))
    else:
        form = ScheduleEditForm(instance=edit_schedule)

    context = {
        'title': 'Занятия/редактирование',
        'form': form
    }
    return render(request, 'adminapp/schedule_create.html', context)


def schedule_delete(request, pk):
    """ Функция для отображения формы удаления нового занятия"""
    schedule = get_object_or_404(Schedule, pk=pk)

    if request.method == 'POST':
        schedule.delete()
        return HttpResponseRedirect(reverse('admin:schedules'))

    context = {
        'title': 'занятия/удаление',
        'schedule_to_delete': schedule
    }

    return render(request, 'adminapp/schedule_delete.html', context)


def progress(request):
    """ Функция для отображения графика прогресса тренирующихся"""
    context = {}
    return render(request, 'adminapp/results.html', context)


def messages(request):
    """ Функция для отображения сообщений из личных кабинетов тренирующихся"""
    messages = Message.objects.all()
    context = {
        'title': 'сообщения',
        'messages': messages,
    }
    return render(request, 'adminapp/messages.html', context)
