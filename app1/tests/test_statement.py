import os
from pathlib import Path
from django.test import TestCase
from app1.models import AdditionalInfoUser, ExamInfo
from app1.views import send_exam_data_xlsx
import pandas as pd

class ExamDataXlsxTests(TestCase):
    def setUp(self):
        user1 = AdditionalInfoUser.objects.create(login="user1", name="Иван Иванов", group="Group1")
        user2 = AdditionalInfoUser.objects.create(login="user2", name="Петр Петров", group="Group2")
        
        ExamInfo.objects.create(login="user1", res="Passed", startTime="2024-10-01T10:00:00Z", time="10:15")
        ExamInfo.objects.create(login="user1", res="Failed", startTime="2024-10-02T11:00:00Z", time="12:30")
        ExamInfo.objects.create(login="user2", res="Passed", startTime="2024-10-03T12:00:00Z", time="14:45")

    def test_send_exam_data_xlsx(self):
        send_exam_data_xlsx()

        file_path = Path("media", "exam_results", "Ведомость.xlsx")
        self.assertTrue(file_path.exists(), "Файл Ведомость.xlsx не был создан")

        df = pd.read_excel(file_path)

        self.assertEqual(len(df), 3)

        self.assertEqual(df.iloc[0]["ФИО/Группа"], "Иван Иванов (Group1)")
        self.assertEqual(df.iloc[0]["Результат"], "Passed")
        self.assertEqual(df.iloc[0]["Дата"], "2024-10-01T10:00:00Z")
        self.assertEqual(df.iloc[0]["Время"], "10:15")

        if file_path.exists():
            os.remove(file_path)
