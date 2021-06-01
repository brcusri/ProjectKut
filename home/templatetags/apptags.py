from django import template
from ProjectKut import settings
from order.models import ShopCart
from  books.models import Category

register = template.Library()

@register.simple_tag
def shopcartcount(userid):
    count = ShopCart.objects.filter(user_id=userid).count()
    return count

@register.simple_tag
def shopcarttotal(userid):
    shopcart = ShopCart.objects.filter(user_id=userid)
    total = 0
    for rs in shopcart:
        total += rs.book.price * rs.quantity
    return total
@register.simple_tag
def shopcartview(userid):
    shopcart = ShopCart.objects.filter(user_id=userid)
    return shopcart

