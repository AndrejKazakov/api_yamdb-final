# Проект YaMDb

### Возможности
- Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
- Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). 
- Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). 
- Добавлять произведения, категории и жанры может только администратор.
- Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
- Пользователи могут оставлять комментарии к отзывам.
- Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Как запустить проект:


* Клонировать репозиторий:

```
git clone https://github.com/katiakate77/api_yamdb.git
```

* В папке с репозиторием создать виртуальное окружение и активировать его:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

* Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

* Выполнить миграции:

```
python3 manage.py migrate
```

* Запустить проект:

```
python3 manage.py runserver
```

### Системные требования
Это приложение написано на языке Python версии 3.8. Для запуска приложения необходимо установить следующие зависимости:

- Django версии 2.2
- DRF

### Стек технологий
- Python
- Django
- DRF
- SQLite
- 
### Примеры
Документация с примерами приведена по адресу: http://127.0.0.1:8000/redoc/

### Авторы и обязанности
##### Первый разработчик (Екатерина)
Пишет всю часть, касающуюся управления пользователями:
- систему регистрации и аутентификации,
- права доступа,
- работу с токеном,
- систему подтверждения через e-mail.

##### Второй разработчик (Андрей)
Пишет модели, view и эндпойнты для
- произведений,
- категорий,
- жанров;
- реализует импорта данных из csv файлов.

##### Третий разработчик (Владимир)
Работает над
- отзывами,
- комментариями,
- рейтингом произведений.
