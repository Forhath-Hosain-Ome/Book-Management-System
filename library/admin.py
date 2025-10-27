from django.contrib import admin
from django.utils.html import format_html
from .models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'isbn', 'cover_preview')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date',)
    readonly_fields = ('cover_preview',)

    fieldsets = (
    (None, {
    'fields': ('title', 'author', 'description')
    }),
    ('Publishing', {
    'fields': ('published_date', 'isbn', 'pages')
    }),
    ('Media', {
    'fields': ('cover', 'cover_preview')
    }),
    )


    def cover_preview(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="max-height:150px;"/>', obj.cover.url)
        return '-'
    cover_preview.short_description = 'Cover preview'