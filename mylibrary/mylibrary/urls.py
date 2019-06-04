from django.conf.urls import url
from django.contrib import admin

from bookshelf import views
from bookshelf import old_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.WelcomeView.as_view()),

    url(r'^my-books/', views.BooksView.as_view(),name="Book"),
    url(r'^book-create$', views.BookCreateView.as_view(),name="bookcreate"),
    url(r'^book-update/(?P<pk>[-\w]+)$', views.BookUpdateView.as_view(),name="bookupdate"),
    url(r'^book-delete/(?P<pk>[-\w]+)$', views.BookDeleteView.as_view(),name="bookdelete"),
    url(r'^book-detail-by-id/(?P<pk>[-\w]+)',
        views.BookDetailByIdView.as_view(),name="bookdetailid"),
    url(r'^book-detail-by-code/(?P<code>[-\w]+)',
        views.BookDetailByCodeView.as_view(),name="bookdetailcode"),
    
    url(r'^my-authors/', views.AuthorView.as_view(),name="Author"), 
    url(r'^author-create$', views.AuthorCreateView.as_view(),name="authorcreate"),
    url(r'^author-update/(?P<pk>[-\w]+)$', views.AuthorUpdateView.as_view(),name="authorupdate"),   
    url(r'^author-delete/(?P<pk>[-\w]+)', views.AuthorDeleteView.as_view(),name="authordelete"),
    

    url(r'^old/my-books/', old_views.get_books_list,name="mbook"),
    url(r'^old/my-authors/', old_views.get_author_list,name="mauthor"),
    url(r'^old/create_Book/',old_views.create_Book,name="mbookcreate"),
    url(r'^old/book-update/(?P<pk>[-\w]+)',
        old_views.edit_book,name="mbookupdate"),
    url(r'^old/book-detail-by-id/(?P<pk>[-\w]+)',
        old_views.get_book_by_id,name="mbookid"),
    url(r'^old/book-detail-by-code/(?P<code>[-\w]+)',
        old_views.get_book_by_code,name="mbookcode"),

    url(r'^old/create_Author/',old_views.create_Author,name="mauthorcreate"),
    url(r'^old/author-update/(?P<pk>[-\w]+)',
        old_views.edit_author,name="mauthorupdate"),
]

