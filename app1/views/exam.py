"""
Модуль для работы с экзаменационными данными, связанными с дорожными знаками.

Содержит функции для:
1. Извлечения данных о знаках и формирования экзаменационных вопросов с ответами, распределенных по сложности.
2. Получения и сохранения данных о прохождении экзамена пользователем, с ограничением на количество записей в базе данных.
"""
import json
import random
from typing import List, Dict, Any

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from app1.models import Exam, ExamInfo


def send_exam(request: HttpRequest) -> JsonResponse:
    """
    Извлекает данные о знаках из базы данных, выбирает вопросы и ответы в зависимости от сложности
    и отправляет их на фронтенд в формате JSON. Гарантированно выбирает 10 вопросов (4 уровня "A", 
    3 уровня "B" и 3 уровня "C") без случайных результатов.
    """
    data = Exam.objects.all().values(
        "complexity", "photo", "realObjectPhoto", "question1", "answer1", 
        "question2", "answer2", "question3", "answer3", "question4", 
        "answer4", "question5", "answer5"
    )

    data_from_database: Dict[str, Any] = {}
    text_questions: List[List[str]] = []
    answers_list: List[List[str]] = []

    for row in data:
        questions = [row["question1"].lower(), row["question2"].lower(), row["question3"].lower(),
                     row["question4"].lower(), row["question5"].lower()]
        answers = [row["answer1"].lower(), row["answer2"].lower(), row["answer3"].lower(),
                   row["answer4"].lower(), row["answer5"].lower()]

        questions = [q for q in questions if q]
        answers = [a for a in answers if a]

        text_questions.append(questions)
        answers_list.append(answers)

    for idx, row in enumerate(data):
        data_from_database[str(idx + 1)] = {
            'number': idx + 1,
            'complexity': row['complexity'],
            'picture': f"/media/{row['photo']}",
            'textQuestions': text_questions[idx],
            'answersList': answers_list[idx],
            'pictureWorld': f"/media/{row['realObjectPhoto']}"
        }

    # Перемешиваем ключи и затем формируем финальный результат
    keys = list(data_from_database.keys())
    random.shuffle(keys)
    shuffled_data = {str(i + 1): data_from_database[key] for i, key in enumerate(keys)}

    # Обеспечиваем точно 10 вопросов с жестким отбором по сложности
    json_data: Dict[int, Dict[str, Any]] = {}
    a_count = 0
    b_count = 0
    c_count = 0
    index = 1

    for item in shuffled_data.values():
        if item['complexity'] == 'A' and a_count < 4:
            json_data[index] = item
            a_count += 1
            index += 1
        elif item['complexity'] == 'B' and b_count < 3:
            json_data[index] = item
            b_count += 1
            index += 1
        elif item['complexity'] == 'C' and c_count < 3:
            json_data[index] = item
            c_count += 1
            index += 1

        if len(json_data) == 10:
            break

    return JsonResponse(json_data)

@csrf_exempt
def get_exam_data(request: HttpRequest) -> JsonResponse:
    """
    Получает и сохраняет данные о прохождении экзамена пользователем.

    Функция проверяет, что пользователь аутентифицирован, получает данные о результате экзамена,
    времени начала и времени прохождения из тела запроса и сохраняет их в базе данных. Если
    количество записей для пользователя превышает 10, самая старая запись удаляется.
    """
    if request.user.is_authenticated:
        username: str = request.user.username
        data: Dict[str, Any] = json.loads(request.body)
        
        t = ExamInfo.objects.create(
            login=username,
            res=data.get('res'),
            startTime=data.get('startTime'),
            time=data.get('time')
        )

        if ExamInfo.objects.filter(login=username).count() > 10:
            ExamInfo.objects.filter(login=username).first().delete()

        t.save(update_fields=["login", "res", "startTime", "time"])

    return JsonResponse({}, status=204)                