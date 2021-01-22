### Основная часть полностью готова. Из бонусов только упаковка в Docker и в нем использование PostgreSQL

### Запуск из виртуального окружения
* Запуск скрипта:
```bash venv.sh```

* Активация виртуального окружения:
```source venv/bin/activate```

* Установка зависимостей:
```pip install -r requirements.txt```

* Создание миграций:
```python manage.py migrate```

* Создать суперпользователя:
```python manage.py createsuperuser```

* Запуск сервера:
```python manage.py runserver ```

### Запуск из контейнера
* Сборка контейнера:
```docker-compose build ```

* Запуск контейнера:
```docker-compose up -d```
   
* Статус контейнера:
```docker-compose logs -f ```

* Остановка контейнера:
```docker-compose down -v```

* Ждем 15-30 секунд, пока **автоматически** произойдут миграции (посредством запуска скрипта entrypoint.sh внутри контейнера)

* Создать суперпользователя:
```docker-compose exec web python manage.py createsuperuser```




### Эндпоинты
* Вход в админку: http://127.0.0.1:8000/admin/
* Регистрация пользователя: http://127.0.0.1:8000/api/rest-auth/registration/
* Авторизация: http://127.0.0.1:8000/api/rest-auth/login/
* Выход из системы: http://127.0.0.1:8000/api/rest-auth/logout/


* Авторы: http://127.0.0.1:8000/api/book_data/authors/
  * Добавить автора http://127.0.0.1:8000/admin/book_data/author/add/
* Книги: http://127.0.0.1:8000/api/book_data/books/
    * Добавить книгу http://127.0.0.1:8000/admin/book_data/book/add/


* Заявка на покупку: http://127.0.0.1:8000/api/requests/purchase/ (только для авторизованных пользователей). После отправки заявки всем администраторам плафтормы с емейлом отправляется письмо

### Бонусы
* PostgreSQL
* Docker

### Дополнительно (не требовалось, доступно только администраторам)
* Список заявок: http://127.0.0.1:8000/api/requests/
* Список юзеров: http://127.0.0.1:8000/api/users/