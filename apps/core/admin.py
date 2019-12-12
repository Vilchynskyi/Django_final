from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Book, Category


class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ('title', 'price')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'in_stock',)
    list_display_links = ('title',)
    list_editable = ('price', 'in_stock')
    readonly_fields = ('pub_date', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    inlines = [BookInline]
