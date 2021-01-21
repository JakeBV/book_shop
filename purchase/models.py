from django.db import models
from django.core.validators import RegexValidator
from simple_history.models import HistoricalRecords

from book_data import models as md


class Request(models.Model):
    """Модель заявки на покупку"""
    user = models.CharField('Пользователь', max_length=255, editable=False)
    book = models.ForeignKey(md.Book, verbose_name='Книга', on_delete=models.CASCADE, related_name='books')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message='Номер телефона необходимо вводить в формате "+78005553535"')
    phone_number = models.CharField('Номер телефона', validators=[phone_regex], max_length=17)
    comment = models.TextField('Комментарий', blank=True)
    date = models.DateTimeField('Дата заявки', auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'Заявка {self.user} на книгу {self.book}'

