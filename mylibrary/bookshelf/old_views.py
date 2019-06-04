from django.http import Http404
from django.shortcuts import redirect, render

from .forms import BookForm,AuthorForm
from .models import Book,Author


def welcome(request):
    return render(request, 'welcome.html')


def get_books_list(request):
    books = Book.objects.all()
    return render(request, 'my-books.html', {'object_list': books})

def get_author_list(request):
    authors = Author.objects.all()
    return render(request, 'my-authors.html', {'object_list': authors})


def get_book_by_id(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
        return render(request, 'my-book-detail.html', {'object': book})


def get_book_by_code(request, code):
    if request.method == 'GET':
        try:
            book = Book.objects.get(code=code)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")
            return render(request, 'my-book-detail.html', {'object': book})


def edit_book(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    if request.method == 'GET':
        form = BookForm(instance=book)
        return render(request, 'my-book-edit.html', {'form': form, 'object': book})

    if request.method == 'POST':
        book = Book.objects.get(id=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/old/my-books')

def create_Author(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("old/my-books")
    else:
        form=AuthorForm()
        context = {'form': form}
    return render(request, 'my-author-create.html',context)

def create_Book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/old/my-books')
    else:
        form=BookForm()
        context = {'form': form}
    return render(request, 'my-book-create.html',context)

def edit_author(request, pk):
    try:
        author = Author.objects.get(id=pk)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

    if request.method == 'GET':
        form = AuthorForm(instance=author)
        return render(request, 'my-author-edit.html', {'form': form, 'object': author})

    if request.method == 'POST':
        author = Author.objects.get(id=pk)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/old/my-books')