from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now

from authapp.forms import FitnessUserRegisterForm
from adminapp.forms import FitnessUserAdminEditForm
from mainapp.models import FitnessUser, ExtractYear


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    year = now().isocalendar()[0]
    users_list = FitnessUser.objects.annotate(
        age=year-ExtractYear('date_birth')).order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username'
    )
    content = {
        'title': 'админка/пользователи',
        'objects': users_list
    	}

    return render(request, 'adminapp/users.html', content)


def user_create(request):

    if request.method == 'POST':
        form = FitnessUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = FitnessUserRegisterForm()
    
    content = {
        'title': 'пользователи/создание', 
        'update_form': form
        }
    
    return render(request, 'adminapp/user_update.html', content)


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
    
    content = {
        'title': 'пользователи/редактирование', 
        'update_form': edit_form
        }
    return render(request, 'adminapp/user_update.html', content)



def user_delete(request, pk):
    user = get_object_or_404(FitnessUser, pk=pk)
    
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': 'пользователи/удаление', 
        'user_to_delete': user
        }
    
    return render(request, 'adminapp/user_delete.html', content)


def trainings(request):
    """ Функция для отображения тренировок """
    pass


def training_create(request):
    """ Функция для отображения формы создания новой тренировки"""
    pass


def training_update(request, pk):
    """ Функция для отображения формы редактирования новой тренировки"""
    pass


def training_delete(request, pk):
    """ Функция для отображения формы удаления новой тренировки"""
    pass


def schedules(request):
    """ Функция для отображения занятий """
    pass


def schedule_create(request):
    """ Функция для отображения формы создания нового занятия"""
    pass


def schedule_update(request, pk):
    """ Функция для отображения формы редактирования нового занятия"""
    pass


def schedule_delete(request, pk):
    """ Функция для отображения формы удаления нового занятия"""
    pass


def progress(request, pk):
    """ Функция для отображения графика прогресса тренирующихся"""
    pass


def messages(request, pk):
    """ Функция для отображения сообщений из личных кабинетов тренирующихся"""
    pass