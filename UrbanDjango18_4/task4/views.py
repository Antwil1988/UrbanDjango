from django.shortcuts import render
from django.urls import reverse


def index(request):
    context = {
        'title': 'Главная страница',
        'index': reverse('index')
    }
    return render(request, 'fourth_task/index.html', context=context)


def page1(request):
    games = {
        'title': 'Магазин',
        'games_list': [
            {'name': 'Atomic Heart'},
            {'name': 'Cyberpunk 2077'},
            {'name': 'Dota 2'},
        ],
        'index': reverse('index')
    }
    return render(request, 'fourth_task/page1.html', context=games)


def page2(request):
    context = {
        'text': 'Здесь будет информация о заказах',
        'title': 'Заказы',
        'index': reverse('index')
    }
    return render(request, 'fourth_task/page2.html', context=context)



