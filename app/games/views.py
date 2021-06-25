from django.shortcuts import render


def games(request):
    return render(request,'games/games.html')

def game(request):
    return render(request,'games/game.html')
