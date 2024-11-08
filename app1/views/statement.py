"""
Модуль для создания и сохранения ведомости экзаменационных данных в формате Excel.
"""

from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
from app1.models import AdditionalInfoUser, ExamInfo
import pandas as pd
import os

@csrf_exempt
def send_exam_data_xlsx():
    """
    Извлекает информацию о прохождении экзамена для всех пользователей,
    создает файл .xlsx (ведомость) и сохраняет его в папку exam_results.

    Данные, включенные в ведомость:
        - ФИО/Группа: Имя пользователя и группа, к которой он принадлежит.
        - Результат: Результат экзамена (сдан/не сдан).
        - Дата: Дата начала экзамена.
        - Время: Время, затраченное на экзамен.
    """
    data = []
    for j in AdditionalInfoUser.objects.all().values("login", "name", "group"):
        for i in ExamInfo.objects.filter(login=j["login"]).values("login", "res", "startTime", "time"):
            i["login"] = f"{j['name']} ({j['group']})"
            data.append(i)

    df = pd.DataFrame({
        'ФИО/Группа': [i['login'] for i in data],
        'Результат': [i['res'] for i in data],
        'Дата': [i['startTime'] for i in data],
        'Время': [i['time'] for i in data]
    })

    output_dir = Path("media", "exam_results")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "Ведомость.xlsx"

    try:
        df.to_excel(output_file, index=False)
    except Exception as e:
        print(f"Ошибка при сохранении файла Excel: {e}")
