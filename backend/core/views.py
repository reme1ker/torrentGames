from django.shortcuts import render
from django.views.generic import DetailView

from backend.core.models import Games


def index(request):
    games = Games.objects.all()
    return render(request, 'index.html', {'title': 'Главная страница сайта',
                                          'games': games})


def about(request):
    return render(request, 'about.html')


class GameDetailView(DetailView):
    model = Games
    template_name = 'game_detail.html'
