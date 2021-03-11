from django.contrib import admin

# Register your models here.
from .models import Film, Serial


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('names', 'kp_rate', 'included')
    list_display_links = ('names',)
    search_fields = ('names', 'included')


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('names', 'included')
    list_display_links = ('names',)
    search_fields = ('names', 'included')
