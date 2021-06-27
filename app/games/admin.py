from django.contrib import admin
from .models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'gameTitle', 'is_trending','is_featured','created_at')
    list_display_links = ('id','gameTitle')
    list_editable = ('is_trending', 'is_featured')
    search_fields = ('gameTitle', 'mainDescription','created_at')
    list_per_page=25


admin.site.register(Game,GameAdmin)
