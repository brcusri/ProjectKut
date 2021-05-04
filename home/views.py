from django.http import HttpResponse
from django.shortcuts import render
from home.models import Settings

# Create your views here.
def index(request):
    setting = Settings.objects.get(pk= 1)
    context = {'setting': setting}
    return render(request, 'index.html', context)