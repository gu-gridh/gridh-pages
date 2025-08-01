from django.contrib import admin
from .models import Page
# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "slug", "content")
