from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# from library.main.models import Book
from .models import Book


def index(request):
    books = Book.objects.all()
    # books = Book.objects.order_by('-id')[:2]
    # books = Book.objects.filter(title='Python')
    return render(request, 'main/index.html', {'title': 'Main page', 'books': books})


def about(request):
    return render(request, 'main/about.html')
    # return HttpResponse('<h4>Hello about</h4>')


def book_view(request):
    return render(request, 'main/about.html')


def book_edit(request):
    return render(request, 'main/about.html')


def book_delete(request, id=0):
    try:
        book = Book.objects.get(id=id)
        book.delete()
    except:
        books = dict({})
    books = Book.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', 'books': books})