from django.shortcuts import render

def index_page(request):
    """
    Данная функция отрисовывает начальную страницу
    """
    return render(request, 'index.html')


def project_page(request):
    """
    Данная функция отрисовывает страницу о нас
    """
    return render(request, 'project-page.html')


def signs_page(request):
    """
    Данная функция отрисовывает страницу со знаками (вкладка "Смотреть")
    """
    return render(request, 'signs-page.html')


def test_page(request):
    """
    Данная функция отрисовывает страницу теста
    """
    return render(request, 'test-page.html')


def exam_page(request):
    """
    Данная функция отрисовывает страницу экзамена
    """
    return render(request, 'exam-page.html')
