from rest_framework import serializers

from .models import Book
from .models import Author


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор книги"""
    author = serializers.CharField()

    class Meta:
        model = Book
        fields = ('title', 'author', 'price')


class AuthorBookSerializer(serializers.ModelSerializer):
    """Сериализатор инфромации о книги в авторе"""

    class Meta:
        model = Book
        fields = ('title', 'price')


class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор автора"""
    books = AuthorBookSerializer(many=True, read_only=True)
    books_count = serializers.IntegerField(source='books.count')

    class Meta:
        model = Author
        fields = ('fio', 'books', 'books_count')
