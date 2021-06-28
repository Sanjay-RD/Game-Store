from django.shortcuts import render
from .models import Game 

def games(request):
    games = Game.objects.all()
    context = {
        'games':games
    }
    return render(request,'games/games.html',context)

def game(request,game_id):
    return render(request,'games/game.html')
