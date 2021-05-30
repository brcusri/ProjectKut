from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from books.models import Category, Book, Images, Comment

class BooksImageInLine(admin.TabularInline):
    model = Images
    extra = 5



class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','amount', 'edition','image_tag','year', 'author']
    list_filter = ['status', 'category']
    readonly_fields = ('image_tag',)
    inlines = [BooksImageInLine]
    prepopulated_fields = {'slug': ('title',)}
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']
    readonly_fields = ('image_tag',)

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Book,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Book,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'book', 'user', 'Status']
    list_filter = ['Status']
    readonly_fields = ('subject', 'comment', 'ip', 'user', 'book', 'rate', 'id')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Images,ImageAdmin)
admin.site.register(Comment,CommentAdmin)


