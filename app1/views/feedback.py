from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Проект_по_созданию_обучающего_сайта_топографических_знаков import settings


@csrf_exempt
def send_to_email(request):
    """
    Данная функция берет данные из формы обратной связи (имя, почта, сообщение) и отправляет нам на почту
    """
    name = request.POST.dict()['name']
    email = request.POST.dict()['email']
    feedback = request.POST.dict()['feedback']
    rating = request.POST.dict()['rating']
    try:
        subject = "studysignsproject"
        send_mail(subject, "Имя: " + name + "\n" + "Почта " + email + "\n" + "Оценка сайта: " + rating + "\n" + "Отзыв: " + feedback, settings.EMAIL_HOST_USER, ['Nikkri20@yandex.ru'])
    except Exception:
        pass

    return JsonResponse({}, status=204)
