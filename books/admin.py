from django.contrib import admin

from books.models import Category, Book, Images

class BooksImageInLine(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent']
    list_filter = ['status']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','amount', 'edition','image_tag','year', 'author']
    list_filter = ['status', 'category']
    readonly_fields = ('image_tag',)
    inlines = [BooksImageInLine]
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    readonly_fields = ('image_tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Images,ImageAdmin)


