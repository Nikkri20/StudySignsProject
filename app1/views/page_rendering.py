"""
Модуль для отображения различных страниц веб-приложения, требующих авторизации.

Этот модуль содержит функции, которые отрисовывают разные страницы приложения, такие как начальная страница,
страница "О нас", страница со знаками, страница теста, страница экзамена и личный кабинет пользователя.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app1.views import send_exam_data_xlsx


@login_required
def index_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает начальную страницу.
    """
    return render(request, 'index.html')


@login_required
def project_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает страницу "О нас".
    """
    return render(request, 'project-page.html')


@login_required
def signs_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает страницу со знаками (вкладка "Смотреть").
    """
    return render(request, 'signs-page.html')


@login_required
def test_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает страницу теста.
    """
    return render(request, 'test-page.html')


@login_required
def exam_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает страницу экзамена.
    """
    return render(request, 'exam-page.html')


@login_required
def account_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает страницу личного кабинета пользователя. Если пользователь является суперпользователем, 
    запускается функция отправки данных экзамена в формате XLSX.
    """
    try:
        if request.user.is_superuser:
            send_exam_data_xlsx()
    except Exception as e:
        print(f"Ошибка при отправке данных экзамена: {e}")  # Логгирование ошибки
    return render(request, 'personal-account-page.html')
