from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


from authapp.forms import FitnessUserLoginForm
from authapp.forms import FitnessUserRegisterForm
from authapp.forms import FitnessUserEditForm


def login(request):

    form = FitnessUserLoginForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
        
            user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('personal:index'))

    content = {
        'title': 'вход', 
        'form': form
        }
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    
    if request.method == 'POST':
        form = FitnessUserRegisterForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = FitnessUserRegisterForm()
    
    content = {
        'title': 'регистрация', 
        'form': form
        }
    
    return render(request, 'authapp/register.html', content)
    
    
def update(request):
    
    if request.method == 'POST':
        form = FitnessUserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = FitnessUserEditForm(instance=request.user)
    
    content = {
        'title': 'редактирование', 
        'form': form
        }
    
    return render(request, 'authapp/update.html', content)  