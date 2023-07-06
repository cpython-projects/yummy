from django.contrib import admin
from .models import MainMenuItem, Footer


@admin.register(MainMenuItem)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Footer)
