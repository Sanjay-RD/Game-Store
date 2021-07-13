from django.contrib import admin
from .models import Review

# Register your models here.
class reviewAdmin(admin.ModelAdmin):
    list_display=('id','user_id','user_name','rating')
    list_display_links=('id',)
    list_per_page = 25


admin.site.register(Review,reviewAdmin)