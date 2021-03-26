from django.contrib import admin

# Register your models here.
from .models import User, Mailing


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id')
    list_display_links = ('name',)
    search_fields = ('name', 'user_id')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('created_at', )
    autocomplete_fields = ('users', )

