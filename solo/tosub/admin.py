from django.contrib import admin

# Register your models here.
from tosub.models import Tosub


class TosubAdmin(admin.ModelAdmin):
    list_display = ('short', 'link')
    list_display_links = ('short',)
    search_fields = ('short', 'link')


admin.site.register(Tosub, TosubAdmin)
