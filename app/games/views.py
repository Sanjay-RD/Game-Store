from django.core import paginator
from django.shortcuts import render,get_object_or_404
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
    game = get_object_or_404(Game,pk=game_id)
    context={
        'game':game
    }
    return render(request, 'games/game.html',context)

def search(request):
    query_list = Game.objects.order_by('-created_at')
    # keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(gameTitle__icontains=keywords)

    context={
        'games':query_list,
        'values':request.GET
    }
    return render(request,'games/search.html',context)
