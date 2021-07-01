from django.core import paginator
from django.shortcuts import render
from .models import Game
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def games(request):
    games = Game.objects.order_by('-created_at')
    paginator = Paginator(games, 3)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)
    context = {
        'games': paged_games
    }
    return render(request, 'games/games.html', context)


def game(request, game_id):
    return render(request, 'games/game.html')
