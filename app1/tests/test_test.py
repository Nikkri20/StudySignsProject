from django.test import TestCase, Client
from django.urls import reverse
from app1.models import Test

class TestDataTests(TestCase):
    def setUp(self):
        # Создаем минимум 5 записей сложности 'A', 5 записей сложности 'B', и 5 записей сложности 'C'
        for i in range(5):
            Test.objects.create(
                complexity='A',
                photo=f'photoA{i}.jpg',
                realObjectPhoto=f'realObjectA{i}.jpg',
                question1='Question A1',
                answer1='Answer A1',
                question2='Question A2',
                answer2='Answer A2',
            )

        for i in range(5):
            Test.objects.create(
                complexity='B',
                photo=f'photoB{i}.jpg',
                realObjectPhoto=f'realObjectB{i}.jpg',
                question1='Question B1',
                answer1='Answer B1',
                question2='Question B2',
                answer2='Answer B2',
            )

        for i in range(5):
            Test.objects.create(
                complexity='C',
                photo=f'photoC{i}.jpg',
                realObjectPhoto=f'realObjectC{i}.jpg',
                question1='Question C1',
                answer1='Answer C1',
                question2='Question C2',
                answer2='Answer C2',
            )


    def test_send_test(self):
        # Отправка GET-запроса к функции send_test
        response = self.client.get(reverse('send_test'))

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200)

        # Проверка структуры JSON-ответа
        data = response.json()
        self.assertEqual(len(data), 10, "Должно быть 10 вопросов в ответе")

        # Проверка распределения по сложности
        complexity_counts = {'A': 0, 'B': 0, 'C': 0}
        for item in data.values():
            self.assertIn('complexity', item)
            self.assertIn('picture', item)
            self.assertIn('textQuestions', item)
            self.assertIn('answersList', item)
            self.assertIn('pictureWorld', item)

            complexity_counts[item['complexity']] += 1

        # Проверка распределения сложности: A - 4, B - 3, C - 3
        self.assertGreaterEqual(complexity_counts['A'], 4, "Должно быть не менее 4 вопросов сложности 'A'")
        self.assertGreaterEqual(complexity_counts['B'], 3, "Должно быть не менее 3 вопросов сложности 'B'")
        self.assertGreaterEqual(complexity_counts['C'], 3, "Должно быть не менее 3 вопросов сложности 'C'")

        # Проверка содержимого одного из вопросов
        question = data['1']
        self.assertTrue(question['textQuestions'])
        self.assertTrue(question['answersList'])
        self.assertTrue(question['picture'])
        self.assertTrue(question['pictureWorld'])
