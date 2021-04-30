from django.contrib import admin

from books.models import Category, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','amount', 'edition', 'year', 'author']
    list_filter = ['status', 'category']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book,BookAdmin)


