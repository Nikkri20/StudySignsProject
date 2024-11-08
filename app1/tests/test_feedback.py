from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail

class FeedbackTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('send_to_email')
        self.user = User.objects.create_user(username='testuser', password='password')

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_send_to_email_authenticated_success(self):
        self.client.login(username='testuser', password='password')
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'feedback': 'Great site!',
            'rating': '5'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 204)

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, "studysignsproject")
        self.assertIn("Имя: Test User", email.body)
        self.assertIn("Почта: test@example.com", email.body)
        self.assertIn("Оценка сайта: 5", email.body)
        self.assertIn("Отзыв: Great site!", email.body)

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
    def test_send_to_email_send_mail_failure(self):
        self.client.login(username='testuser', password='password')
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'feedback': 'Great site!',
            'rating': '5'
        }
        
        with self.assertRaises(Exception):
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, 500)
