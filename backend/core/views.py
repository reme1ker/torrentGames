from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.response import Response

from backend.core.models import Games, Categories
from rest_framework.views import APIView

from core.serializers import ReviewCreateSerializer, ReviewSerializer, GameDetailSerializer


def index(request):
    # games_list = Games.objects.all()
    # paginator = Paginator(games_list, 10)
    # page = request.GET.get('page')
    # try:
    #          games = paginator.page(page)
    # except PageNotAnInteger:
    #             games = paginator.page(1)
    # except EmptyPage:
    #        games = paginator.page(paginator.num_pages)
    # games = dict(
    #     games=games,
    # )
    games = Games.objects.all()
    categories = Categories.objects.all()
    return render(request, 'mainContent.html', {'title': 'Главная страница сайта',
                                                'games': games,
                                                'categories': categories
                                                })


def card(request):
    return render(request, 'card.html')


class GameDetailView(DetailView):
    model = Games
    template_name = 'game_detail.html'


class ReviewCreateView(APIView):
    """Добавление отзыва к фильму"""

    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class GameSDetailView(APIView):
    """Вывод фильма"""

    def get(self, request, pk):
        movie = Games.objects.get(id=pk)
        serializer = GameDetailSerializer(movie)
        return Response(serializer.data)
