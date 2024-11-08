"""
Модуль для управления пользовательскими данными и профилями в системе.

Функции обеспечивают проверку аутентификации, а также обработку ошибок для корректного взаимодействия с фронтендом.
"""

import logging
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from app1.models import AdditionalInfoUser, ExamInfo


@csrf_exempt
def get_account_data(request: HttpRequest) -> JsonResponse:
    """
    Обновляет данные пользователя в личном кабинете.

    Функция проверяет, аутентифицирован ли пользователь, и если да, обновляет
    информацию о пользователе (имя, группа, статус суперпользователя, аватар) в базе данных.
    Возвращает JSON-ответ с результатом операции.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Пользователь не аутентифицирован"}, status=403)

    try:
        username = request.user.username
        user_info = AdditionalInfoUser.objects.get(login=username)

        # Обновляем поля, если они присутствуют в запросе
        name = request.POST.get('name')
        group = request.POST.get('group')
        is_superuser = request.user.is_superuser

        if name:
            user_info.name = name
        if group:
            user_info.group = group
        user_info.is_superuser = is_superuser

        # Обновляем аватар, если файл был передан
        if 'avatar' in request.FILES:
            user_info.avatar = request.FILES['avatar']

        user_info.save(update_fields=["name", "group", "avatar", "is_superuser"])

        return JsonResponse({"message": "Данные успешно сохранены"}, status=200)

    except AdditionalInfoUser.DoesNotExist:
        logging.error(f"Пользователь с логином {username} не найден")
        return JsonResponse({"error": "Пользователь не найден"}, status=404)
    except KeyError as e:
        logging.error(f"Ошибка при доступе к данным: {e}")
        return JsonResponse({"error": "Неправильный формат данных запроса"}, status=400)
    except Exception as e:
        logging.error(f"Ошибка сохранения данных: {e}")
        return JsonResponse({"error": "Не удалось сохранить данные"}, status=500)


def send_account_data(request: HttpRequest) -> JsonResponse:
    """
    Возвращает данные профиля пользователя для отображения в личном кабинете.

    Функция проверяет, аутентифицирован ли пользователь. Если да, извлекает данные
    из базы, включая аватар, имя, группу, статус пользователя, и email.
    Возвращает JSON-ответ с данными пользователя.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Пользователь не аутентифицирован"}, status=403)

    try:
        username = request.user.username
        info = AdditionalInfoUser.objects.get(login=username)

        data = {
            'avatar': f'/media/{info.avatar}' if info.avatar else '',
            'name': info.name or '',
            'group': info.group or '',
            'is_superuser': info.is_superuser,
            'email': username
        }
        return JsonResponse(data, status=200)

    except AdditionalInfoUser.DoesNotExist:
        logging.error(f"Пользователь с логином {username} не найден")
        return JsonResponse({"error": "Пользователь не найден"}, status=404)
    except Exception as e:
        logging.error(f"Ошибка при получении данных пользователя: {e}")
        return JsonResponse({"error": "Произошла ошибка при получении данных"}, status=500)


def send_exam_data(request: HttpRequest) -> JsonResponse:
    """
    Возвращает последние 10 записей о результатах экзамена пользователя для отображения в личном кабинете.

    Функция проверяет, аутентифицирован ли пользователь. Если да, извлекает до 10 последних
    записей о результатах экзамена из базы данных, включая статус, дату начала, и время прохождения.
    Возвращает JSON-ответ с результатами экзаменов.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Пользователь не аутентифицирован"}, status=403)

    try:
        # Получаем последние 10 записей для данного пользователя
        exam_results = list(
            ExamInfo.objects.filter(login=request.user.username)
            .values("res", "startTime", "time")
            .order_by('-id')[:10]
        )

        if not exam_results:
            return JsonResponse({"message": "Нет данных для отображения"}, status=200)

        return JsonResponse({"results": exam_results}, status=200)

    except Exception as e:
        logging.error(f"Ошибка при получении данных экзамена: {e}")
        return JsonResponse({"error": "Произошла ошибка при получении данных"}, status=500)
