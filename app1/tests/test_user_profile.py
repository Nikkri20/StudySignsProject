from django.test import TestCase, Client
from django.contrib.auth.models import User
from app1.models import AdditionalInfoUser, ExamInfo
from django.urls import reverse

class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()

        self.additional_info = AdditionalInfoUser.objects.create(
            login='testuser',
            name='Test User',
            group='Group 1',
            is_superuser=False
        )

        for i in range(15):
            ExamInfo.objects.create(
                login='testuser',
                res=f'Result {i+1}',
                startTime='2024-01-01T00:00:00Z',
                time='00:30:00'
            )

    def test_get_account_data_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('get_account_data'), {
            'name': 'Updated Name',
            'group': 'Updated Group'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('message'), 'Данные успешно сохранены')
        self.additional_info.refresh_from_db()
        self.assertEqual(self.additional_info.name, 'Updated Name')
        self.assertEqual(self.additional_info.group, 'Updated Group')

    def test_get_account_data_not_authenticated(self):
        response = self.client.post(reverse('get_account_data'))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json().get('error'), 'Пользователь не аутентифицирован')

    def test_send_account_data_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('send_account_send'))

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data.get('name'), 'Test User')
        self.assertEqual(data.get('group'), 'Group 1')
        self.assertEqual(data.get('is_superuser'), 'False')

    def test_send_account_data_not_authenticated(self):
        response = self.client.get(reverse('send_account_send'))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json().get('error'), 'Пользователь не аутентифицирован')

    def test_send_exam_data_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('send_exam_send'))

        self.assertEqual(response.status_code, 200)
        data = response.json().get('results')
        self.assertEqual(len(data), 10)
        self.assertEqual(data[0]['res'], 'Result 15')

    def test_send_exam_data_not_authenticated(self):
        response = self.client.get(reverse('send_exam_send'))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json().get('error'), 'Пользователь не аутентифицирован')