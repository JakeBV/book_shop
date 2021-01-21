from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author
from .models import Book
from .serializers import AuthorSerializer
from .serializers import BookSerializer


class AuthorsView(APIView):
    """Просмотр авторов"""
    @staticmethod
    def get(request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({'authors': serializer.data})


class BooksView(APIView):
    """Просмотр книг"""
    @staticmethod
    def get(request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})
