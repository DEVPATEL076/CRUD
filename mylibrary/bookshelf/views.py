from django.views.generic import (CreateView, DetailView, ListView, TemplateView,
                                  UpdateView)
from django.views.generic.edit import DeleteView
from .forms import AuthorForm, BookForm
from .models import Author, Book


class WelcomeView(TemplateView):
    template_name = 'welcome.html'

#--------------------------------------------------------Book

class BooksView(ListView):
    model = Book
    template_name = 'my-books.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'my-book-create.html'
    form_class = BookForm
    success_url = '/my-books'

class BookDetailByIdView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'


class BookDetailByCodeView(DetailView):
    model = Book
    template_name = 'my-book-detail.html'
    
    def get_object(self):
        return Book.objects.get(code=self.kwargs['code'])


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'my-book-edit.html'
    form_class = BookForm
    success_url = '/my-books'

class BookDeleteView(DeleteView):
    model = Book
    success_url = '/my-books'

#-----------------------------------------------------------Author

class AuthorView(ListView):
    model = Author
    template_name = 'my-authors.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'my-author-create.html'
    form_class = AuthorForm
    success_url = '/my-authors'

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'my-author-edit.html'
    form_class = AuthorForm
    success_url = '/my-authors'

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/my-authors'

 
  

