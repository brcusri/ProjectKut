from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string

from books.models import Book, Category
from home.models import UserProfile
from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderBook, WishBook


def index(request):
    return HttpResponse("Order App")

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkbook = ShopCart.objects.filter(book_id=id)
    if checkbook:
        control = 1 # The product is in the cart
    else:
        control = 0 # not
    if request.method == 'POST': # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data = ShopCart.objects.get(book_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.book_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, 'product added to cart')
            return HttpResponseRedirect(url)
    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(book_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.book_id = id
            data.quantity = 1
            data.save()
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, 'product added to cart')
        return HttpResponseRedirect(url)

    messages.warning(request,'adding product failed')
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    total = 0
    for rs in shopcart:
        total += rs.book.price * rs.quantity
    contex = {
        'category': category,
        'shopcart':shopcart,
        'total': total
    }
    return render(request,'ShopCartBook.html',contex)

@login_required(login_url='/login')
def deletefromcart(request,id):
    current_user = request.user
    ShopCart.objects.filter(id=id).delete()
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request,"Successfully deleted")
    return HttpResponseRedirect("/shopcart")


def OrderBookFunc(request):
    category = Category.objects.all()
    curent_user = request.user
    shopcart = ShopCart.objects.filter(user_id=curent_user.id)
    total = 0
    for rs in shopcart:
        total += rs.book.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.adress = form.cleaned_data['adress']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = curent_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()  # random cod
            data.code = ordercode
            data.save()

            shopcart = ShopCart.objects.filter(user_id=curent_user.id)
            for rs in shopcart:
                detail = OrderBook()
                detail.order_id = data.id
                detail.book_id = rs.book_id
                detail.user_id = curent_user.id
                detail.quantity = rs.quantity
                detail.price = rs.book.price
                detail.amount = rs.amount
                detail.save()

                book = Book.objects.get(id=rs.book_id)
                book.amount -= rs.quantity
                book.save()

            ShopCart.objects.filter(user_id=curent_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request,"Your order has been completed. Thank you")
            return render(request,'OrderCompleted.html',{'ordercode':ordercode,'category':category})
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/order/orderbook")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=curent_user.id)
    context = {
        'category': category,
        'shopcart':shopcart,
        'total':total,
        'profile':profile,
        'form':form,
    }
    return render(request,'OrderForm.html',context)

def wishlist(request):
    category = Category.objects.all()
    current_user = request.user
    wishbook = WishBook.objects.filter(user_id=current_user.id)
    request.session['wish_items'] = WishBook.objects.filter(user_id=current_user.id).count()
    contex = {
        'category': category,
        'wishbook': wishbook,
    }
    return render(request, 'WishListBook.html', contex)

@login_required(login_url='/login')
def addwishlist(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkbook = WishBook.objects.filter(book_id=id)
    if checkbook:
        control = 1
    else:
        control = 0

    if control == 1:
        data = WishBook.objects.get(book_id=id)
        data.quantity += 1
        data.save()
    else:
        data = WishBook()
        data.user_id = current_user.id
        data.book_id = id
        data.quantity = 1
        data.save()
    messages.success(request, 'Book added to wishlist')
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def deletefromwish(request,id):
    current_user = request.user
    WishBook.objects.filter(id=id).delete()
    request.session['wish_items'] = WishBook.objects.filter(user_id=current_user.id).count()
    messages.success(request,"Successfully deleted")
    return HttpResponseRedirect("/order/wishlist")

