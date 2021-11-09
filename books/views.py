from django.shortcuts import render, redirect
from .forms import BookForm

from books.models import Books
from django.http import HttpResponseRedirect

# Create your views here.


def list_books(request):
    books = Books.objects.all().order_by("title")
    return render(request, "books/list_books.html", {"books": books})


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    return render(request, "books/add_book.html", {"form": form})

def delete_book(request, pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        book.delete();
        return HttpResponseRedirect('/')
    else:
        return render(request, 'books/delete_book.html', {'book':book})
    

def edit_book(request, pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author_name = request.POST['author_name']
        book.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'books/edit_book.html', {'book': book})