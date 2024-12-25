from django.shortcuts import render
from django.urls import reverse


def index(request):
    context = {
        'title': 'Главная страница',
        'index': reverse('index')
    }
    return render(request, 'third_task/index.html', context=context)


def page1(request):
    games = {
        'games_list': [
            {'name': 'Игра 1'},
            {'name': 'Игра 2'},
            {'name': 'Игра 3'},
        ],
        'index': reverse('index')
    }
    return render(request, 'third_task/page1.html', context=games)


def page2(request):
    context = {
        'index': reverse('index')
    }
    return render(request, 'third_task/page2.html', context=context)
