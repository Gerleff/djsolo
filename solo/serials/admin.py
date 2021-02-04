from django.contrib import admin

# Register your models here.

from serials.models import Serials


class SerialsAdmin(admin.ModelAdmin):
    list_display = ('names', 'included')
    list_display_links = ('names',)
    search_fields = ('names', 'included')


admin.site.register(Serials, SerialsAdmin)
