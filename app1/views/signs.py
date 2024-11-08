"""
Модуль для обработки данных о знаках и их категориях.
"""

from django.http import JsonResponse, HttpRequest
from app1.models import Sign, Category
from typing import Dict, Any

def send_signs(request: HttpRequest) -> JsonResponse:
    """
    Извлекает информацию о знаках из базы данных и отправляет на фронтенд (страница "Смотреть").
    """
    signs = Sign.objects.all().values("name", "description", "category", "photo", "realObjectPhoto")
    data_from_database: Dict[str, Dict[str, Any]] = {}

    for idx, row in enumerate(signs, start=1):
        data_from_database[str(idx)] = {
            'name': row['name'],
            'description': row['description'],
            'category': row['category'],
            'picture': f"/media/{row['photo']}" if row['photo'] else None,
            'pictureWorld': f"/media/{row['realObjectPhoto']}" if row['realObjectPhoto'] else None
        }

    return JsonResponse(data_from_database)


def send_categories(request: HttpRequest) -> JsonResponse:
    """
    Извлекает информацию о категориях из базы данных и отправляет на фронтенд для фильтрации
    (страница "Смотреть").
    """
    categories = Category.objects.all().values("name", "description", "category")
    data_from_database: Dict[str, Dict[str, Any]] = {}

    for idx, row in enumerate(categories, start=1):
        data_from_database[str(idx)] = {
            'name': row['name'],
            'description': row['description'],
            'category': row['category']
        }

    return JsonResponse(data_from_database)
