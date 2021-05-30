from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


from books.models import Comment,CommentForm

# Create your views here.
def index(request):
    return HttpResponse("Product Page")


@login_required(login_url='login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.book_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request,"Your comment has been sent successfully!")
            return HttpResponseRedirect(url)
    messages.warning(request, "Operation Failed")
    return HttpResponseRedirect(url)
