from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blogTitle', 'user_id', 'published_date')
    list_display_links = ('id', 'blogTitle')
    list_filter = ('user_name',)
    search_fields = ('blogTitle', 'blogDescription')
    list_per_page = 20


admin.site.register(Blog, BlogAdmin)
