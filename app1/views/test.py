"""
Модуль для получения данных о тестах и отправки их на фронтенд.

Этот модуль содержит функцию `send_test`, которая извлекает вопросы и ответы из базы данных,
распределяет их по сложности и отправляет их в формате JSON для использования на фронтенде.
Тестовые вопросы и ответы проходят фильтрацию на пустые значения, и результат
случайным образом сортируется.
"""

import random
from django.http import JsonResponse
from django.http import HttpRequest
from app1.models import Test
from typing import Dict, Any, List

def send_test(request: HttpRequest) -> JsonResponse:
    """
    Извлекает из базы данных информацию о тестах, удаляет пустые вопросы и ответы,
    распределяет их по сложности, сортирует случайным образом и отправляет на фронтенд.
    """
    data = Test.objects.all().values("complexity", "photo", "realObjectPhoto", 
                                     "question1", "answer1", "question2", "answer2", 
                                     "question3", "answer3", "question4", "answer4", 
                                     "question5", "answer5")

    data_from_database: Dict[str, Dict[str, Any]] = {}
    textQuestions: List[List[str]] = []
    answersList: List[List[str]] = []

    for row in data:
        questions = [q.lower() for q in [row["question1"], row["question2"], row["question3"], 
                                         row["question4"], row["question5"]] if q]
        answers = [a.lower() for a in [row["answer1"], row["answer2"], row["answer3"], 
                                       row["answer4"], row["answer5"]] if a]

        textQuestions.append(questions)
        answersList.append(answers)

    for idx, row in enumerate(data, start=1):
        data_from_database[str(idx)] = {
            'number': idx,
            'complexity': row['complexity'],
            'picture': f"/media/{row['photo']}",
            'textQuestions': textQuestions[idx - 1],
            'answersList': answersList[idx - 1],
            'pictureWorld': f"/media/{row['realObjectPhoto']}"
        }

    keys = list(data_from_database.keys())
    random.shuffle(keys)
    shuffled_data = {str(i + 1): data_from_database[key] for i, key in enumerate(keys)}

    for i, item in enumerate(shuffled_data.values(), start=1):
        item["number"] = i

    json_data: Dict[int, Dict[str, Any]] = {}
    index = 0

    # Отбираем по 4 вопроса сложности 'A'
    for item in shuffled_data.values():
        if item['complexity'] == 'A' and len([q for q in json_data.values() if q['complexity'] == 'A']) < 4:
            index += 1
            json_data[index] = item

    # Отбираем по 3 вопроса сложности 'B'
    for item in shuffled_data.values():
        if item['complexity'] == 'B' and len([q for q in json_data.values() if q['complexity'] == 'B']) < 3:
            index += 1
            json_data[index] = item

    # Отбираем по 3 вопроса сложности 'C'
    for item in shuffled_data.values():
        if item['complexity'] == 'C' and len([q for q in json_data.values() if q['complexity'] == 'C']) < 3:
            index += 1
            json_data[index] = item

    return JsonResponse(json_data)
