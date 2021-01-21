from django.urls import path

from .views import AuthorsView
from .views import BooksView

urlpatterns = [
    path('authors/', AuthorsView.as_view()),
    path('books/', BooksView.as_view()),
]
