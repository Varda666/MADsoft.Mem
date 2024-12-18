from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    list_filter = ('email', 'name')
    search_fields = ('email', 'name')



