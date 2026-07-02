from django.contrib import admin
from .models import Page, NavigationItem
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug", "content")


@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ("label", "page", "external_url", "order", "open_in_new_tab")
    list_editable = ("order")
