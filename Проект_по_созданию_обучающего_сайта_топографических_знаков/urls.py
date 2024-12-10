"""Проект_по_созданию_обучающего_сайта_топографических_знаков URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('project-page/', views.project_page, name='project'),
    path('signs-page/', views.signs_page, name='signs'),
    path('test-page/', views.test_page, name='test'),
    path('exam-page/', views.exam_page, name='exam'),
    path('signs-page/send_signs', views.send_signs, name='send_signs'),
    path('test-page/send_test', views.send_test, name='send_test'),
    path('exam-page/send_exam', views.send_exam, name='send_exam'),
    path('signs-page/send_categories', views.send_categories, name='send_categories'),
    path('test-page/send_to_email', views.send_to_email, name="send_to_email"),
    path('exam-page/send_to_email', views.send_to_email, name="send_to_email"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)