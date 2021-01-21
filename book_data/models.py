from django.db import models


class Book(models.Model):
    """Модель книги"""
    author = models.ForeignKey('Author', verbose_name='Автор', on_delete=models.PROTECT,
                               related_name='books')
    title = models.CharField('Название', max_length=255, unique=True)
    price = models.PositiveSmallIntegerField('Цена')

    def __str__(self):
        return self.title


class Author(models.Model):
    """Модель автора"""
    fio = models.CharField('Фамилия Имя Отчество', max_length=255, unique=True)

    def __str__(self):
        return self.fio
