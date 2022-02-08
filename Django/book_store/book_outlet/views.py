from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html',{ "books":books})

def book_info(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, "book_details.html",{
        "title":book.title,"autho":book.author,"rating":book.rating,"is_bestseller":book.is_bestselling
    })