from django.contrib import admin

# Register your models here.
from solo.ivi.models import Film, Serial


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    pass