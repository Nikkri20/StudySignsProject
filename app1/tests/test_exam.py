import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app1.models import Exam, ExamInfo

class ExamDataTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_send_exam(self):
        for _ in range(10):
            Exam.objects.create(
                complexity='A', photo='photo1.jpg', realObjectPhoto='object1.jpg',
                question1='What is this sign?', answer1='Answer1',
                question2='Second question?', answer2='Answer2'
            )
        for _ in range(10):
            Exam.objects.create(
                complexity='B', photo='photo2.jpg', realObjectPhoto='object2.jpg',
                question1='What does this mean?', answer1='AnswerB1',
                question2='Another question?', answer2='AnswerB2'
            )
        for _ in range(10):
            Exam.objects.create(
                complexity='C', photo='photo3.jpg', realObjectPhoto='object3.jpg',
                question1='Identify this sign', answer1='AnswerC1',
                question2='Explain this', answer2='AnswerC2'
            )

        response = self.client.get(reverse('send_exam'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 10)
        
        complexity_counts = {"A": 0, "B": 0, "C": 0}
        for item in data.values():
            complexity_counts[item['complexity']] += 1

        self.assertGreaterEqual(complexity_counts["A"], 4)
        self.assertGreaterEqual(complexity_counts["B"], 3)
        self.assertGreaterEqual(complexity_counts["C"], 3)

    def test_get_exam_data_authenticated(self):
        self.client.force_login(self.user)
        
        data = {
            "res": "passed",
            "startTime": "2024-10-26T10:00:00Z",
            "time": "10:15"
        }
        
        response = self.client.post(
            reverse('get_exam_data'),
            data=json.dumps(data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 204)
        self.assertTrue(ExamInfo.objects.filter(login="testuser").exists())

        exam_info = ExamInfo.objects.get(login="testuser")
        self.assertEqual(exam_info.res, "passed")
        self.assertEqual(exam_info.startTime, "2024-10-26T10:00:00Z")
        self.assertEqual(exam_info.time, "10:15")

    def test_get_exam_data_limit_records(self):
        for i in range(12):
            ExamInfo.objects.create(
                login="testuser",
                res="passed",
                startTime="2024-10-26T10:00:00Z",
                time="10:15"
            )

        while ExamInfo.objects.filter(login="testuser").count() > 10:
            oldest_record = ExamInfo.objects.filter(login="testuser").first()
            oldest_record.delete()

        self.assertEqual(ExamInfo.objects.filter(login="testuser").count(), 10)
