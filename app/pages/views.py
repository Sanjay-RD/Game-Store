from django.shortcuts import render
from games.models import Game

# views is use to render .html template

# index is function that we pass from urls ie-> views.index


def index(request):
    # Get Trending game
    trending_game = Game.objects.all().filter(is_trending=True)[:4]
    # Get featured game
    featured_game = Game.objects.all().filter(is_featured=True)[:4]
    # Get latest game
    latest_game = Game.objects.order_by('-created_at')[:4]

    context = {
        'trending_game':trending_game,
        'featured_game':featured_game,
        'latest_game':latest_game
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

def cart(request):
    return render(request, 'pages/cart.html')

