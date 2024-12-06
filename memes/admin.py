from django.contrib import admin
from memes.models import Mem


@admin.register(Mem)
class MemAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'text', 'owner', 'image',
    )
    list_filter = (
        'name', 'text', 'owner', 'image',
    )
    search_fields = (
        'name', 'text', 'owner', 'image',
    )


