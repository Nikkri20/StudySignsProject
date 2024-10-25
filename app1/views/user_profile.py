"""
Этот модуль содержит функции для управления пользовательскими данными и профилями в системе.
"""
import logging

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from app1.models import AdditionalInfoUser, ExamInfo


@csrf_exempt
def get_account_data(request: HttpRequest) -> JsonResponse:
    """
    Обрабатывает запрос на обвновление информации о пользователе в личном кабинете. 
    
    Функция проверяет то, аутентифицирован ли пользователь, и если да, обновляет данные 
    пользователя (имя, группу, статус пользователя, аватар) в базе данных. 
    Возвращает JSON-ответ с результатом операции.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Пользователь не аутентифицирован"}, status=403)

    try:
        username = request.user.username
        t = AdditionalInfoUser.objects.get(login=username)

        name = request.POST.get('name')
        group = request.POST.get('group')
        is_superuser = request.user.is_superuser
        
        if name:
            t.name = name 
        if group:
            t.group = group  
        t.is_superuser = is_superuser

        if 'avatar' in request.FILES:
            t.avatar = request.FILES['avatar']

        t.save(update_fields=["name", "group", "avatar", "is_superuser"])

        return JsonResponse({"message": "Данные успешно сохранены"}, status=200)

    except AdditionalInfoUser.DoenNotExist:
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
    Возвращает данные о пользователе для отображения в личном кабинете.
    
    Функция проверяет аутентифицирован ли пользователь. Если да, извлекает информацию
    из базы данных, включая аватар, имя, группу, статус пользователя.
    Возвращает JSON-ответ с результатом операции.
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

    except AdditionalInfoUser.DoenNotExist:
        data = {"error": "Пользователь не найден"}
    except Exception as e:
        logging.error(f"Ошибка при получении данных пользователя: {e}")
        data = {"error": "Произошла ошибка при получении данных"}
    return JsonResponse(data)

def send_exam_data(request: HttpRequest) -> JsonResponse:
    """
    Возвращает информацию о результатах прохождения экзамена для отображения в личном кабинете.

    Функция проверяет, аутентифицирован ли пользователь. Если да, извлекает до 10 последних записей
    из базы данных, содержащих информацию о результатах экзамена, времени начала и времени прохождения.
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

        # Проверяем, есть ли данные
        if not exam_results:
            return JsonResponse({"message": "Нет данных для отображения"}, status=200)

        # Возвращаем данные в формате JSON
        return JsonResponse({"results": exam_results}, status=200)

    except Exception as e:
        logging.error(f"Ошибка при получении данных экзамена: {e}")
        return JsonResponse({"error": "Произошла ошибка при получении данных"}, status=500)