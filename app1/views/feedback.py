"""
Модуль для обработки и отправки данных из формы обратной связи на указанный email.

Этот модуль содержит функцию `send_to_email`, которая обрабатывает данные из формы обратной связи, 
включая имя, email, отзыв и рейтинг пользователя. Функция проверяет, что пользователь аутентифицирован, 
извлекает данные из запроса и отправляет их на заранее указанный адрес электронной почты. 
В случае успешной отправки возвращается пустой JSON-ответ со статусом 204, а при ошибке — соответствующий статус и сообщение.
"""

from django.core.mail import send_mail
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def send_to_email(request: HttpRequest) -> JsonResponse:
    """
    Обрабатывает данные из формы обратной связи и отправляет их на указанный email.

    Функция проверяет, что пользователь аутентифицирован, затем получает данные 
    из формы (имя, email, отзыв, рейтинг) и отправляет их на указанный адрес электронной почты.
    В случае ошибки при отправке email возвращает пустой ответ с кодом 500.
    """
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Пользователь не аутентифицирован"}, status=403)

    name = request.POST.get('name')
    email = request.POST.get('email')
    feedback = request.POST.get('feedback')
    rating = request.POST.get('rating')

    if not all([name, email, feedback, rating]):
        return JsonResponse({"error": "Все поля формы обязательны"}, status=400)

    try:
        subject = "studysignsproject"
        message = f"Имя: {name}\nПочта: {email}\nОценка сайта: {rating}\nОтзыв: {feedback}"
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['Nikkri20@yandex.ru'])
    except Exception as e:
        return JsonResponse({"error": "Не удалось отправить сообщение"}, status=500)

    return JsonResponse({}, status=204)
