instert_article - принимает POST-ом json с контентом статьи (строка), создает запись в таблице в бд, у корой есть ид и контент статьи
пример {"content": "текст статьи"}

instert_comments - принимает POST-ом json с ид статьи и текстом комментария, создает запись в таблице в бд, у которой ид статьи, ид комментария и текст комментария
пример {"pk": "1", "text": "Hello World"}

repost -  принимает POST-ом json с ид родителя комментария и текстом комментария,  создает запись в таблице в бд, у которой ид статьи, ид комментария, ид родителя и текст комментария (по сути создает комментарий, в ответ на другой комментарий)
пример {"pk": "1", "text": "Sound like a good idea"}

get_article_comments - принимает POST-ом json с ид статьи и возвращает массив всех вложенных комментариев до 3-го уровня вложенности
пример {"pk": "1"}

get_all_sub_comments - принимает POST-ом json с ид статьи и возвращает массив всех вложенных комментариев
пример {"pk": "1"}



для запуска приложения необходимо установить:
Django - pip install django
psycopg2 - pip install psycopg2


Не забудь сделать миграции:
python manage.py makemigrations
python manage.py migrate


в файле settings.py в переменной DATABASES заполнить своими данными:
'NAME': '***',
'USER': ***
'PASSWORD': '***',
'HOST': '***',
'PORT': '5432',
 