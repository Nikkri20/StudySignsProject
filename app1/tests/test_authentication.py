from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app1.models import AdditionalInfoUser
from django.contrib.messages import get_messages
from app1.views import configure_form_username_field


class UserAccountTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_configure_form_username_field(self):
        form = UserCreationForm()
        configure_form_username_field(form)
        self.assertEqual(form.fields['username'].label, "Почта")
        self.assertEqual(form.fields['username'].help_text, "Почта должна быть выдана организацией УрФУ")

    def test_sign_up_view_get_request(self):
        response = self.client.get(reverse('registr'))
        self.assertTemplateUsed(response, 'registr.html')
        self.assertEqual(response.status_code, 200)

    def test_sign_up_view_post_valid(self):
        response = self.client.post(reverse('registr'), {
            'username': 'test@urfu',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='test@urfu').exists())

    def test_sign_up_view_post_invalid_email(self):
        response = self.client.post(reverse('registr'), {
            'username': 'test@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertTemplateUsed(response, 'registr.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Пожалуйста, используйте почту организации УрФУ.")
        self.assertFalse(User.objects.filter(username='test@example.com').exists())

    def test_sign_in_view_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')
        self.assertEqual(response.status_code, 200)

    def test_sign_in_view_post_valid(self):
        User.objects.create_user(username='test@urfu', password='Password123!')
        response = self.client.post(reverse('login'), {
            'username': 'test@urfu',
            'password': 'Password123!',
        })
        self.assertRedirects(response, reverse('index'))

    def test_sign_in_view_post_invalid_credentials(self):
        User.objects.create_user(username='test@urfu', password='Password123!')
        response = self.client.post(reverse('login'), {
            'username': 'test@urfu',
            'password': 'WrongPassword',
        })
        self.assertTemplateUsed(response, 'login.html')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Неправильное имя пользователя или пароль.")
