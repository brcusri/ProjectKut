from django.contrib import admin

from order.models import ShopCart,Order, OrderBook,WishBook


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'price', 'quantity', 'amount']
    list_filter = ['user']

class WishBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'quantity']
    list_filter = ['user']

class OrderBookline(admin.TabularInline):
    model = OrderBook
    readonly_fields = ('user', 'book','price','quantity','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'adress', 'city', 'country', 'phone', 'first_name', 'ip', 'last_name', 'phone', 'city', 'total')
    can_delete = False
    inlines = [OrderBookline]

class OrderBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book','price','quantity','amount']
    list_filter = ['user']


admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderBook,OrderBookAdmin)
admin.site.register(WishBook,WishBookAdmin)