from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderbook/', views.OrderBookFunc, name='orderbook'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('addwishlist/<int:id>', views.addwishlist, name='addwishlist'),
    path('deletefromwish/<int:id>', views.deletefromwish, name='deletefromwish'),

    #path('addcomment/<int:id>',views.addcomment, name='addcomment')
]