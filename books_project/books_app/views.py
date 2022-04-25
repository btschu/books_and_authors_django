from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        'books' : Book.objects.all(),
    }
    if request.method == 'GET':
        return render(request, 'books.html', context)
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        return redirect('/')

def authors(request):
    context = {
        'authors' : Author.objects.all(),
    }
    if request.method == 'GET':
        return render(request, 'authors.html', context)
    if request.method == 'POST':
        # book_id = Book.objects.get(id=int(request.POST['book']))
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        return redirect('/authors')

def one_book(request, id):
    context = {
        'book' : Book.objects.get(id=id),
        'authors' : Author.objects.all(),
    }
    if request.method == 'GET':
        return render(request, 'one_book.html', context)
    if request.method == 'POST':
        this_author = Author.objects.get(id = request.POST['book'])
        this_book = Book.objects.get(id = id)
        this_author.book.add(this_book)
        return redirect(f'/books/{id}')

def one_author(request, id):
    context = {
        'author' : Author.objects.get(id=id),
        'authors' : Author.objects.all(),
        'books' : Book.objects.all(),
    }
    if request.method == 'GET':
        return render(request, 'one_author.html', context)
    if request.method == 'POST':
        this_author = Author.objects.get(id = id)
        this_book = Book.objects.get(id = request.POST['book'])
        this_author.book.add(this_book)
        return redirect(f'/authors/{id}')