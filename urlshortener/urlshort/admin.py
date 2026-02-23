from django.contrib import admin
from .models import URL, UrlModel


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url')


@admin.register(UrlModel)
class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'original_url', 'short_url')
