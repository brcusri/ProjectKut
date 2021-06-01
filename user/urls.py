from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('userorders/', views.user_orders, name='userorders'),
    path('orderdetail/<int:id>', views.order_detail, name='orderdetail'),
    path('comments/', views.comments, name='comments'),
    path('deletecomments/<int:id>', views.deletecomments, name='deletecomments'),
    #path('addcomment/<int:id>',views.addcomment, name='addcomment')
]