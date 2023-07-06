from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import DishCategory, Dish, Gallery, Event, ContactInfoItem


admin.site.register(Gallery)
admin.site.register(Event)
admin.site.register(ContactInfoItem)

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'category', 'name', 'position', 'price', 'weight', 'photo_src_tag', 'is_visible')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('category', 'position', 'price', 'weight', 'is_visible')
    list_filter = ('category', 'price')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Dish photo'