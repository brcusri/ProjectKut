from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from books.models import Book
from home.models import Settings, ContactForm, ContactFormMessage

# Create your views here.
def index(request):
    setting = Settings.objects.get(pk= 1)
    sliderdata = Book.objects.all()[:4]
    context = {'setting': setting,
               'page':'home',
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)

def AboutUs(request):
    setting = Settings.objects.get(pk= 1)
    context = {'setting': setting, 'page': 'AboutUs'}
    return render(request, 'AboutUs.html', context)

def References(request):
    setting = Settings.objects.get(pk= 1)
    context = {'setting': setting, 'page': 'References'}
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
    form =ContactForm
    context = {'setting': setting, 'form': form}
    return render(request, 'Contact.html', context)