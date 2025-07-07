# Проект «Сайт агенства недвижимости»
Это Django-приложение для хранения информации о квартирах, собственниках квартир.

## Особенности

Удобное отображение связанных квартир и собственников в админке Django

Возможность быстрого поиска квартир по характеристикам и собственникам

## Установка и запуск
1. Клонировать репозиторий:
```
git clone <url_репозитория>
cd <папка_проекта>
```
2. Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Установить зависимости:
```
pip install -r requirements.txt
```
4. Создать миграции и применить их:
```
python manage.py makemigrations
python manage.py migrate
```
5. Запустить сервер:
```
python manage.py runserver
```
### Перенос данных собственников
Чтобы перенести данные из полей owner и owners_phonenumber модели Flat в связанную модель Owner, используется дата-миграция:

Создайте пустую миграцию:
```
python manage.py makemigrations --empty property
```
Выполните миграцию:
```
python manage.py migrate
```

