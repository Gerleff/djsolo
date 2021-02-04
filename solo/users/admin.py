from django.contrib import admin

# Register your models here.
from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_id')
    list_display_links = ('name',)
    search_fields = ('name', 'user_id')


admin.site.register(User, UserAdmin)
