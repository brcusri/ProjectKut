"""ProjectKut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from home import views
from user import views as UserViews
from order import views as  OrderViews



urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('books/', include('books.urls')),
    path('user/', include('user.urls')),
    path('order/',include('order.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('Refences/', views.References, name='References'),
    path('Contact/', views.Contact, name='Contact'),


    path('category/<int:id>/<slug:slug>', views.category_product, name='category_product'),
    path('book/<int:id>/<slug:slug>',views.book_detail, name='book_detail'),
    path('search/',views.book_search, name='book_search'),
    path('search_auto/', views.book_search_auto, name='book_search_auto'),


    path('signup/', UserViews.signup_view, name='signup_view'),
    path('logout/', UserViews.logout_view, name='logout_view'),
    path('login/', UserViews.login_view, name='login_view'),

    path('shopcart/', OrderViews.shopcart, name='shopcart'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
