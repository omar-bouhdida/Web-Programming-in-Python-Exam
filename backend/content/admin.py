from django.contrib import admin
from .models import PageContent

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content_type', 'is_published', 'publish_date', 'created_at')
    list_filter = ('is_published', 'content_type', 'created_at', 'author')
    search_fields = ('title', 'body', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
