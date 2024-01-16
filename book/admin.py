from django.contrib import admin
from .models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author','name','price')
    list_display_links = ('author','name','price')
    ordering = ('name',)