"""
Модуль для обработки регистрации и входа пользователей на сайт.

Содержит функции для настройки форм, регистрации новых пользователей и аутентификации.
Позволяет пользователям регистрироваться с использованием почты, выданной организацией УрФУ,
а также обеспечивает обработку входа, выхода и отображение сообщений об ошибках.
"""
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django import forms

from app1.models import AdditionalInfoUser


def configure_form_username_field(form: forms.Form) -> None:
    """
    Настраивает поле 'username' для форм регистрации и входа.

    Функция изменяет метку и текст помощи поля 'username' в переданной форме,
    устанавливая метку на "Почта" и указывая, что почта должна быть выдана организацией УрФУ.
    """
    username_field = form.fields['username']
    username_field.label = "Почта"
    username_field.help_text = "Почта должна быть выдана организацией УрФУ"

def sign_up(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает регистрацию нового пользователя.

    Если пользователь уже аутентифицирован, перенаправляет его на главную страницу.
    Если запрос - POST, обрабатывает форму регистрации, проверяет, что почта
    соответствует требованиям, и сохраняет нового пользователя. В случае успешной
    регистрации перенаправляет на страницу входа. Если форма невалидна или запрос не POST,
    отображает форму регистрации.
    """
    if request.user.is_authenticated:
        return redirect('index')

    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        configure_form_username_field(form)

        # Проверка валидации формы и соответствия почты организации
        if form.is_valid() and '@urfu' in form.cleaned_data['username']:
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            return redirect('login')
        else:
            messages.error(request, "Пожалуйста, используйте почту организации УрФУ.")
    else:
        form = UserCreationForm()
        configure_form_username_field(form)

    data['form'] = form
    return render(request, 'registr.html', data)


def sign_in(request: HttpRequest) -> HttpResponse:
    """
    Обрабатывает вход пользователя в систему.

    Если пользователь уже аутентифицирован, выполняет его выход и отображает форму входа.
    Если запрос - POST, проверяет данные формы, аутентифицирует пользователя и выполняет вход.
    В случае успешного входа обновляет или создает запись в модели `AdditionalInfoUser`.
    Если данные формы неверны или запрос не POST, отображает форму входа.
    """
    if request.user.is_authenticated:
        logout(request)

    form = AuthenticationForm(request, data=request.POST or None)
    configure_form_username_field(form)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            info, created = AdditionalInfoUser.objects.get_or_create(login=user.username)
            if not created:
                info.save()
            return redirect('index')
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")

    return render(request, 'login.html', {'form': form})
