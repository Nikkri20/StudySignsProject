from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import os

class PageRenderingTests(TestCase):
    def setUp(self):
        # Инициализация клиента и создание тестового пользователя
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_page(self):
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project-page.html')

    def test_signs_page(self):
        response = self.client.get(reverse('signs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signs-page.html')

    def test_test_page(self):
        response = self.client.get(reverse('test'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'test-page.html')

    def test_exam_page(self):
        response = self.client.get(reverse('exam'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exam-page.html')

    def test_account_page_for_regular_user(self):
        # Проверяем, что обычный пользователь может получить доступ к странице аккаунта
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personal-account-page.html')
