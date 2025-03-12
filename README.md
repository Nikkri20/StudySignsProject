## Cайт для изучения студентами условных топографических знаков

https://github.com/user-attachments/assets/cfb8beea-1c82-40e0-b369-a884a3a13b12

___
## Команда 🤝

### Backend-разработчик: Крылов Никита Андреевич 🛠️
### Frontend-разработчик: Карболин Сергей Александрович 🖥️
### Дизайнер: Стратюк Лада Александровна 🖌️

___

> [!NOTE]
> Данная документация по проекту была написана Backend-разработчиком, возможно неточности

> [!WARNING]
> Проект развивается, по возможности буду стараться обновлять всю информацию

<a name="0"></a>

## Оглавление 📄
#### Общая информация
* [Для кого это](#1) 👥
* [Описание проекта](#2) 📝
* [Стек технологий](#3) 📚
  
#### Для разработчиков
* [Структура проекта](#4) 🗂️
* [Схематично как устроен проект на данный момент на хосте](#5) 🗂️
* [Как развернуть проект](#6) ⬇️
* [Про базы данных](#7) 🗄
___

## Общая информация
___

<a name="1"></a>

### Для кого это 👥
* Для тех, кто будет продолжать или поддерживать данный проект
* Для нас самих же, чтобы не забыть как функционирует проект

[К оглавлению](#0) ⬆️
___

<a name="2"></a>

### Описание проекта 📝

Web-система с базой данных всего массива условных топографических знаков и их характеристик, дающая возможность тренироваться в чтении условных топографических знаков и позволяющая контролировать полученные знания с помощью теста и экзамена

[К оглавлению](#0) ⬆️
___

<a name="3"></a>

### Стек технологий 📚
#### Frontend
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/183568594-85e280a7-0d7e-4d1a-9028-c8c2209e073c.png" width="100" />
</p>

#### Backend
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" width="100" />
  <img src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/117207330-263ba280-adf4-11eb-9b97-0ac5b40bc3be.png" width="100" />
  <img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" width="100" />
</p>

#### Дизайн
<img src="https://user-images.githubusercontent.com/25181517/189715289-df3ee512-6eca-463f-a0f4-c10d94a06b2f.png" width="100" />

#### Хост

<img src="https://github.com/user-attachments/assets/b9c286e7-6a8f-4623-8b47-e68dbb6e8788" width="100" />

#### Дополнительные технологии

<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" width="100" />
  <img src="https://www.svglogos.net/wp-content/uploads/Google_Meet_icon_28202029.svg" width="100" />
  <img src="https://github.com/user-attachments/assets/9ff4ca83-7114-4521-9e44-a6573325d9f6" width="100" />
</p>
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/183345125-9a7cd2e6-6ad6-436f-8490-44c903bef84c.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/192108372-f71d70ac-7ae6-4c0d-8395-51d8870c2ef0.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/192108374-8da61ba1-99ec-41d7-80b8-fb2f7c0a4948.png" width="100" />
</p>

[К оглавлению](#0) ⬆️
___

<a name="4"></a>

### Структура проекта 🗂️

```
├─ app1
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ tests
│  │  ├─ __init__.py
│  │  ├─ test_exam.py
│  │  ├─ test_feedback.py
│  │  ├─ test_page_rendering.py
│  │  ├─ test_signs.py
│  │  └─ test_test.py
│  ├─ views
│  │  ├─ __init__.py
│  │  ├─ exam.py
│  │  ├─ feedback.py
│  │  ├─ page_rendering.py
│  │  ├─ signs.py
│  │  └─ test.py
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  └─ models.py
├─ media
│  ├─ exam_results
│  │  └─ .gitignore
│  └─ img
│     └─ personal-img.png
├─ node_modules
│  └─ .package-lock.json
├─ static
│  ├─ css
│  │  ├─ admin.css
│  │  ├─ exam-page-style.css
│  │  ├─ index-style.css
│  │  ├─ personal-account-page-style.css
│  │  ├─ project-page-style.css
│  │  ├─ registration-login.css
│  │  ├─ signs-page-style.css
│  │  └─ test-page-style.css
│  ├─ easytimer.js
│  │  ├─ .github
│  │  │  └─ workflows
│  │  │     └─ ci.yml
│  │  ├─ dist
│  │  │  ├─ easytimer.js
│  │  │  ├─ easytimer.min.js
│  │  │  ├─ examples.min.css
│  │  │  └─ examples.min.js
│  │  ├─ src
│  │  │  ├─ easytimer
│  │  │  │  ├─ easytimer.js
│  │  │  │  ├─ eventEmitter.js
│  │  │  │  ├─ leftPadding.js
│  │  │  │  └─ timeCounter.js
│  │  │  └─ examples
│  │  │     ├─ examples.js
│  │  │     └─ jquery.js
│  │  ├─ test
│  │  │  ├─ timer.spec.html
│  │  │  └─ timer.spec.js
│  │  ├─ .eslintrc.json
│  │  ├─ .gitignore
│  │  ├─ .npmignore
│  │  ├─ LICENSE.md
│  │  ├─ MIGRATION.md
│  │  ├─ README.md
│  │  ├─ bower.json
│  │  ├─ index.d.ts
│  │  ├─ index.html
│  │  ├─ package-lock.json
│  │  ├─ package.json
│  │  ├─ rollup.config.examples.mjs
│  │  └─ rollup.config.mjs
│  ├─ img
│  │  ├─ Rectangle 5.svg
│  │  ├─ account-logo.svg
│  │  ├─ button-close.png
│  │  ├─ curator-1.jpg
│  │  ├─ curator-2.jpg
│  │  ├─ dark-icon.svg
│  │  ├─ exam-logo.svg
│  │  ├─ icon-download.png
│  │  ├─ member-1.jpg
│  │  ├─ member-2.jpg
│  │  ├─ member-3.jpg
│  │  ├─ personal-img.png
│  │  ├─ registr-fon.png
│  │  ├─ role-icon.png
│  │  ├─ sign-filter.png
│  │  ├─ sign-logo.svg
│  │  ├─ test-logo.svg
│  │  └─ urfu-logo.png
│  └─ js
│     ├─ pages
│     │  ├─ exam
│     │  │  ├─ changeCard.js
│     │  │  ├─ fillQuestionCard.js
│     │  │  ├─ finish.js
│     │  │  ├─ getDataExam.js
│     │  │  ├─ index.js
│     │  │  └─ review.js
│     │  ├─ profile
│     │  │  ├─ backData.js
│     │  │  ├─ editData.js
│     │  │  ├─ fillAccount.js
│     │  │  ├─ fillResults.js
│     │  │  ├─ index.js
│     │  │  └─ saveData.js
│     │  ├─ signs
│     │  │  ├─ activeFilter.js
│     │  │  ├─ fillingFilters.js
│     │  │  ├─ fillingSigns.js
│     │  │  ├─ index.js
│     │  │  ├─ openCard.js
│     │  │  └─ showMore.js
│     │  └─ test
│     │     ├─ changeCard.js
│     │     ├─ fillQuestionCard.js
│     │     ├─ getDataTest.js
│     │     └─ index.js
│     ├─ changeRating.js
│     ├─ form.js
│     └─ theme.js
├─ templates
│  ├─ admin
│  │  └─ base_site.html
│  ├─ base.html
│  ├─ exam-page.html
│  ├─ index.html
│  ├─ login.html
│  ├─ personal-account-page.html
│  ├─ project-page.html
│  ├─ registr.html
│  ├─ signs-page.html
│  └─ test-page.html
├─ Проект_по_созданию_обучающего_сайта_топографических_знаков
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ .gitignore
├─ Dockerfile
├─ Makefile
├─ README.md
├─ docker-build.sh
├─ docker-compose.yml
├─ manage.py
├─ nginx.conf
├─ package-lock.json
├─ package.json
└─ requirements.txt
```

<a name="5"></a>

### Схематично как устроен проект на данный момент на хосте

![image](https://github.com/user-attachments/assets/e902fe13-ae34-44e5-8b57-fbde71bea121)

[К оглавлению](#0) ⬆️
___

<a name="6"></a>

### Как развернуть проект ⬇️

> [!NOTE]
> Далее используются команды Bash (лучше повторять эти шаги в Bash терминале, если вы используете Windows, то можно вводить эти команды, например, в Git Bash, WSL или PyCharm).
Если вы используете Linux, то Bash доступен в стандартом терминале по умолчанию

1. Клонируем репозиторий 

```
git clone https://github.com/Nikkri20/StudySignsProject
```

2. Переходим в дирректорию проекта

```
cd StudySignsProject
```

3. (Необязательно) Создаем .venv (чтобы не засорять вашу систему нашими зависимостями. При удалении проекта удалятся и все зависимости, которые мы установим далее)

```
python -m venv
```

4. Установим зависимости из requirements.txt

```
pip install -r requirements.txt
```
> [!WARNING]
> Дальнейшие шаги могут вызывать ошибки, если проект не найдет базу данных
>
> [Про базы данных](#7) 🗄

5. Создаем миграции, чтобы база данных обновилась в соответствии с моделями

```
python manage.py makemigrations
```

6. Запускаем миграции

```
python manage.py migrate
```

7. Создаем суперпользователя (запоминаем логин/пароль, именно с этими данными мы будем заходить в админку на сайте)

```
python manage.py createsuperuser
```

8. (Необязательно) Добавляем пароль приложений (чтобы информация из формы доходила до почты)

`settings.py`
```Python
EMAIL_HOST_PASSWORD = "Мы предоставим пароль"
```

9. Запускаем сайт

```
python manage.py runserver
```

[К оглавлению](#0) ⬆️
___

<a name="7"></a>

### Про базы данных 🗄

Прежде чем начать детальное рассмотрение нашей базы данных попробуем посмотреть на проект с высоты птичьего полета. Сайт создан для того, чтобы пользователи смогли изучать знаки. В данный момент функционал сделан таким образом, что знаки добавляются суперпользователем через админку, потом, силами Django, эти данные попадают в базу данных и выводятся на сайте

![image](https://github.com/Nikkri20/StudySignsProject/assets/114663524/5cd69479-7a0e-4857-91c9-88f98d5ee5cd)

Знак это не только одна картинка. С каждым знаком идет набор характеристик: описание, сложность, вопросы к тесту/экзамену, категория, фото реального объекта и.т.п. Всё это нужно хранить где-то, поэтому в нашей базе данных существует таблица `sign`

Отдельная таблица `category` у нас отведена под категории для знаков

Для аккаунтов у нас есть таблица `additionalinfouser`

Для сбора результатов экзамена у нас есть таблица `examinfo`

![image](https://github.com/Nikkri20/StudySignsProject/assets/114663524/136c6a16-b132-4ed0-a84d-a13cd65b5872)


> [!TIP]
> На данный момент у нас есть уже рабочая база даных на хосте (в которой хранится 500+ знаков)

[К оглавлению](#0) ⬆️
___
