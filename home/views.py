from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from books.models import Book, Category, Images, Comment
from home.models import Settings, ContactForm, ContactFormMessage, UserProfile
from home.forms import SearchForm
import  json

# Create your views here.
from order.models import ShopCart


def index(request):
    current_user = request.user
    setting = Settings.objects.get(pk= 1)
    sliderdata = Book.objects.all()[:4]
    category = Category.objects.all()
    daybooks = Book.objects.order_by('-amount')[:4]
    bestbooks = Book.objects.all().order_by('-id')[:4]
    pickbooks = Book.objects.all().order_by('?')[:4]
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'daybooks': daybooks,
               'bestbooks': bestbooks,
               'pickbooks': pickbooks,
               'category': category,
               }
    return render(request, 'index.html', context)

def AboutUs(request):
    setting = Settings.objects.get(pk= 1)
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'AboutUs',
               'category':category}
    return render(request, 'AboutUs.html', context)

def References(request):
    setting = Settings.objects.get(pk= 1)
    category = Category.objects.all()
    context = {'setting': setting,
               'page': 'References',
               'category':category}
    return render(request, 'References.html', context)

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız Gönderilmiştir. Teşekkürler!")
            return HttpResponseRedirect('/Contact')
    setting = Settings.objects.get(pk= 1)
    category = Category.objects.all()
    form =ContactForm()
    context = {'setting': setting,
               'form': form,
               'category':category}
    return render(request, 'Contact.html', context)

def category_product(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    books = Book.objects.filter(category_id=id)
    context = {
        'books':books,
        'category': category,
        'categorydata':  categorydata,
        'slug': slug,
    }
    return render(request,'Books.html',context)

def book_detail(request,id,slug):
    category = Category.objects.all()
    book = Book.objects.get(pk=id)
    Image = Images.objects.filter(books_id=id)
    comments = Comment.objects.filter(book_id=id,Status=True)
    context = {
        'category': category,
        'book': book,
        'Image': Image,
        'comments': comments,
    }
    return render(request, 'book_detail.html', context)

def book_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                books = Book.objects.filter(title__icontains=query)
            else:
                books = Book.objects.filter(title__icontains=query,category_id=catid)
            context = {
                'category': category,
                'books':books}
            return render(request,'search.html',context)
    return HttpResponseRedirect('/')

def book_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        book = Book.objects.filter(edition__icontains=q)
        results = []
        for rs in book:
            book_json = {}
            book_json = rs.title
            results.append(book_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)


