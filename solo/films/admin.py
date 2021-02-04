from django.contrib import admin

# Register your models here.

from films.models import Films


class FilmsAdmin(admin.ModelAdmin):
    list_display = ('names', 'kp_rate', 'included')
    list_display_links = ('names',)
    search_fields = ('names', 'included')


admin.site.register(Films, FilmsAdmin)
