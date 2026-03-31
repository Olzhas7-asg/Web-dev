# shop-back — Django REST API

Backend API для интернет-магазина (Lab 8).

## Установка и запуск

```bash
# 1. Создать виртуальное окружение
python -m venv venv

# 2. Активировать (Windows)
venv\Scripts\activate

# Активировать (Mac/Linux)
source venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py migrate

# 5. Запустить сервер
python manage.py runserver
```

## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/products/` | Список всех продуктов |
| GET | `/api/products/<id>/` | Один продукт по ID |
| GET | `/api/categories/` | Список всех категорий |
| GET | `/api/categories/<id>/` | Одна категория по ID |
| GET | `/api/categories/<id>/products/` | Продукты по категории |

## Структура проекта

```
shop-back/
├── manage.py
├── requirements.txt
├── .gitignore
├── shop_back/          # настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/                # приложение
    ├── models.py       # модели Category и Product
    ├── views.py        # вьюхи (логика эндпоинтов)
    ├── urls.py         # маршруты
    ├── admin.py
    └── migrations/
```
