# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Users
from .forms import UserForm

def check(request):
    data = {
        'error': "",

    }
    # users = Users.objects.all()
    if request.method == 'POST':
        nickname = request.POST['nickname']
        try:
            user = Users.objects.get(nickname=nickname)
            # Нікнейм знайдений у базі даних
            # Виконайте відповідні дії тут
            data['error'] = 'Нікнейм вже використовується'
            return render(request, 'main/login.html')
        except Users.DoesNotExist:
            # Нікнейм не знайдений у базі даних
            # Виконайте відповідні дії тут
            data['error'] = 'Нікнейм вільний'
            return render(request, 'main/register.html')

    return render(request, 'main/check.html', data)

def register(request):
    error = ""
    if request.method == 'POST':
        form = UserForm(request.POST)
        # Перевіряє чи всі дані коректно визначені
        if form.is_valid():
            form.save()
            return redirect('check')
        else:
            error = "Некоректно заповнена форма!"
    else:
        form = UserForm()

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/register.html', data)


def login(request):
    error = ""
    if request.method == 'POST':
        form = UserForm(request.POST)
        # Перевіряє чи всі дані коректно визначені
        if form.is_valid():
            form.save()
            return redirect('check')
        else:
            error = "Некоректно заповнена форма!"

    form = UserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/login.html', data)