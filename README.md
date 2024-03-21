## Cайт для изучения студентами условных топографических знаков

![Снимок экрана 2024-03-19 150319](https://github.com/Nikkri20/StudySignsProject/assets/114663524/e918c86e-f8f4-4813-b7fe-00a006be71b6)
___
## Команда 🤝

### Backend-разработчик: Крылов Никита Андреевич 🛠️
### Frontend-разработчик: Карболин Сергей Александрович 🖥️
### Дизайнер: Стратюк Лада Александровна 🖌️

___

> [!NOTE]
> Данная документация по проекту была написана Backend-разработчиком (соответственно взгляд на проект может быть не полный). Я попытаюсь описать структуру проекта, описать проблемы и почему были приняты те или иные решения

> [!WARNING]
> Проект развивается, по возможности буду стараться обновлять всю информацию

## Оглавление 📄
#### Общая информация
* [Для кого это](#1)
* [Описание проекта](#2)
* [Стек технологий](#3)
  
#### Для разработчиков
* [Структура проекта](#4)
* [Как развернуть проект](#5)
* [Про базы данных](#6)

#### Для пользователей

#### Прочее
* [Планы](#7)
___

## Общая информация
___

<a name="1"></a>

### Для кого это 👥
* Для тех, кто будет продолжать данный проект (eсли кто-то будет)
* Для интересующихся
* Для нас самих же, чтобы не забыть как функционирует проект

___

<a name="2"></a>

### Описание проекта 📝

Web-система с базой данных всего массива условных топографических знаков и их характеристик, дающая возможность тренироваться в чтении условных топографических знаков и позволяющая контролировать полученные знания с помощью теста и экзамена

___

<a name="3"></a>

### Стек технологий 📚
#### Frontend
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" width="100" />
</p>
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png" width="100" />
  <img src="https://user-images.githubusercontent.com/25181517/183568594-85e280a7-0d7e-4d1a-9028-c8c2209e073c.png" width="100" />
</p>

#### Backend
<p float="left">
  <img src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" width="100" />
  <img src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" width="100" />
</p>

#### Дизайн
<img src="https://user-images.githubusercontent.com/25181517/189715289-df3ee512-6eca-463f-a0f4-c10d94a06b2f.png" width="100" />

#### Дополнительные технологии, которые помогают работать над проектом

![PythonAnywhere](https://img.shields.io/badge/pythonanywhere-%232F9FD7.svg?style=for-the-badge&logo=pythonanywhere&logoColor=151515)

![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

![Trello](https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white)

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

___

## Для разработчиков
___

<a name="4"></a>

### Структура проекта 🗂️

> [!NOTE]
> Кратко описал предназначение каждого элемента для быстрого вкатывания в проект, для более подробной и точной информации лучше ознакомиться с официальной документацией Django: https://docs.djangoproject.com/en/5.0/ 

>📁 **app1 (_файлы приложения app1_)**

>>📁 **migrations (_папка для хранения миграций_)**

>>>📄 **__init__.py (_файл, который показывает python, что эта дирректория является пакетом_)**

>>📄 **__init__.py (_файл, который показывает python, что эта дирректория является пакетом_)**

>>📄 **admin.py (_файл для отображения моделей в админке_)**

>>📄 **apps.py (_настройка приложения_)**

>>📄 **forms.py (_файл для работы с формами_)**

>>📄 **models.py (_файл для создания моделей_)**

>>📄 **tests.py (файл для создания тестов)**

>>📄 **views.py (_Представления (Views) — главные составляющие веб-приложений на основе Django_)**

>📁 **node_modules (_папка с модулями для Node.js_)**

>>📄 **.package-lock.json (_описывает прямые зависимости и их версии + зависимости наших зависимостей, которые использует JavaScript_)**

>📁 **static (_статические файлы_)**

>>📁 **css (_css страниц_)**

>>>📄 **admin.css (_админка_)**

>>>📄 **exam-page-style.css (_страница экзамена_)**

>>>📄 **index-style.css (_главная страница_)**

>>>📄 **personal-account-page-style.css (_аккаунт пользователя_)**

>>>📄 **registration-login.css (_страница входа_)**

>>>📄 **signs-page-style.css (_страница со списком знаков_)**

>>>📄 **test-page-style.css (_тест_)**

>>📁 **easytimer.js (_библиотека для js_)**

>>>📑 **...**

>>📁 **examresults (_папка с результатами экзамена_)**

>>>📄 **ведомость.pdf (ведомость)**

>>📁 **fonts (_папка для шрифтов для ведомости_)**

>>>📄 **...**

>>📁 **img (_папка с изображениями для сайта_)**

>>>📑 **...**

>>📁 **js (_js коды страниц_)**

>>>📄 **const.js (_константы_)**

>>>📄 **exam-page.js (_страница экзамена_)**

>>>📄 **index.js (_список знаков_)**

>>>📄 **personal-account-page.js (_страница аккаунта пользователя_)**

>>>📄 **test-page.js (__страница теста__)**

>📁 **templates (_html-шаблоны страниц_)**

>>📁 **admin (_html-шаблны для работы с админкой_)**

>>>📄 **base_site.html (_админка (щаблон унаследован от стандартного шаблона админки)_)**

>>📄 **base.html (_страница регистрации и входа в аккаунт (шаблон унаследован от стандартных шаблонов страниц регистрации и входа в аккаунт)_)**

>>📄 **exam-page.html (_страница экзамена_)**

>>📄 **index.html (_главная страница_)**

>>📄 **login.html (_страница входа_)**

>>📄 **personal-account-page.html (_аккаунт пользователя_)**

>>📄 **project-page.html (_страница о нас_)**

>>📄 **registr.html (_страница регистрации_)**

>>📄 **signs-page.html (_список знаков_)**

>>📄 **test-page.html (_страница теста_)**

>📁 **Проект_по_созданию_обучающего_сайта_топографических_знаков (_содержит основные настройки нашего проекта_)**

>>📄 **__init__.py (_файл, который показывает python, что эта дирректория является пакетом_)**

>>📄 **asgi.py (_файл для деплоя проекта на сервер (асинхронно)_)**

>>📄 **settings.py (_основные настройки Django_)**

>>📄 **urls.py (_url-конфиг, этот файл описывает зависимости между выражениями URL-пути и функциями отображениями views_)**

>>📄 **wsgi.py (_файл для деплоя проекта на сервер (синхронно)_)**

>📄 **.gitignore (_файл, который указывает Git что не отслеживать в проекте_)**

>📄 **README.md (_файл с информацией о проекте_)**

>📄 **manage.py (_является ссылкой на скрипт django-admin, но с уже предустановленными переменными окружения, указывающими на ваш проект, как для чтения настроек оттуда, так и для управления им при необходимости_)**

>📄 **package-lock.json (_описывает прямые зависимости и их версии + зависимости наших зависимостей, которые использует JavaScript_)**

>📄 **package.json (_описывает прямые зависимости и их версии, которые использует JavaScript_)**

>📄 **requirements.txt (_файл, содержащий список пакетов или библиотек, необходимых для работы над проектом, которые желательно установить перед запуском_)**

___

<a name="5"></a>

### Как развернуть проект ⬇️

> [!WARNING]
> На данный момент есть проблема с запуском на системах с Linux. Связано это с тем, что при работе с fpdf генерируется windows-путь

> [!NOTE]
> Далее используются команды Bash (лучше повторять эти шаги в Bash терминале, если вы используете Windows, то можно воспользоваться данным терминалом, например, в Git Bash, WSL или PyCharm).
Если вы используете Linux, то Bash доступен в стандартом терминале по умолчанию

1. Клонируем репозиторий 

```
git clone https://github.com/Nikkri20/StudySignsProject
```

2. Переходим в дирректорию проекта

```
cd StudySignsProject
```

3. Создаем .venv (чтобы не засорять вашу систему нашими зависимостями. При удалении проекта удалятся и все зависимости, которые мы установим далее)

```
python -m venv
```

4. Установим зависимости из requirements.txt

```
pip install -r requirements.txt
```

5. Создаем миграции, чтобы база данных обновилась в соответствии с моделями

```
python manage.py makemigrations
```

6. Запускаем миграции

```
python manage.py migrate
```

7. Создаем суперпользователя (запоминаем логин/пароль, именно с этими данными мы будем заходить в аккаунт на сайте)

```
python manage.py createsuperuser
```

8. Запускаем сайт

```
python manage.py runserver
```
___

<a name="6"></a>

### Про базы данных 🗄

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Прежде чем начать детальное рассмотрение нашей базы данных попробуем посмотреть на проект с высоты птичьего полета. Сайт создан для того, чтобы пользователи смогли изучать знаки. В данный момент функционал сделан таким образом, что знаки добавляются суперпользователем через админку, потом, силами Django, эти данные попадают в базу данных и выводятся на сайте

> Схематично попытался изобразить это

![image](https://github.com/Nikkri20/StudySignsProject/assets/114663524/5cd69479-7a0e-4857-91c9-88f98d5ee5cd)

Знак это не только одна картинка. С каждым знаком идет набор характеристик: описание, сложность, вопросы к тесту/экзамену, категория, фото реального объекта и.т.п. Всё это нужно хранить где-то, поэтому в нашей базе данных существует таблица `sign`

Отдельная таблица `category` у нас отведена под категории для знаков

Для аккаунтов у нас есть таблица `additionalinfouser`

Для сбора результатов экзамена у нас есть таблица `examinfo`

> Изобразил более подробно структуру базы данных

![image](https://github.com/Nikkri20/StudySignsProject/assets/114663524/136c6a16-b132-4ed0-a84d-a13cd65b5872)


> [!TIP]
> На данный момент у нас есть уже рабочая база даных на хосте (в которой хранится 500+ знаков)

___

## Для пользователей 👨🏻‍💻👨🏻‍💻👨🏻‍💻

___

### Для суперпользователя 🧑🏻‍💻👑

При заходе на сайт нас встречает страница регистрации

Нас интересует страница входа в аккаунт, введите логин/пароль от аккаунта, который обладает статусом "Суперпользователь"

> [!WARNING]
> Если вы развернули проект на своей машине, то введите те данные, которые вы вводили при создании суперпользователя

Перейдем в личный кабинет, нажав на соответсвующую иконку справа-сверху

Тут мы можем скачать  ведомость (ведомость содержит в себе данные о пользователе и 10 последних попыток экзамена)

Суперпользователь может самостоятельно добавлять знаки через админку. Переходим на главную страницу, добавляем в адресную строку /admin, вводим логин/пароль, которые мы выдали

> [!WARNING]
> Если вы развернули проект на своей машине, то введите те данные, которые вы вводили при создании суперпользователя

Если вам нужна новая категория для знаков, добавляем её через соответствующую вкладку, после добавления категория появится в фильтре на странице `Посмотреть`

Чтобы добавить знак, переходим на соответствующую вкладку, заполняем все поля и нажимаем добавить, если всё хорошо, то ваш знак появится на странице `Посмотреть` (не забудьте перейти на нужную категорию через фильтр)

> [!WARNING]
> Вы могли заметить, что мы можем выбрать фиксированную сложность знаков через выпадающее меню, вероятно, было бы удобнее сделать тоже самое с категориями, я подумал также, но эти выпадающие менюшки обновляются только при перезагрузке проетка. Сложность это фиксированный набор данных, категории же мы можем добавять в любой момент, но новая категория не появится до тех пор, пока не будет перезагружен сервер. Это временная проблема, она возникает из-за ограничений админки django, в будущем планируется перенести функционал добавления категорий/знаков из админки в личный кабинет (тогда данные будут обновляться сразу же, как обновляются остальные поля в личном кабинете)

### Для пользователя 🧑🏻‍💻

При заходе на сайт нас встречает страница регистрации, вводим наши данные (почта должна заканчиваться на .urfu). Запонимаем данные, они нам будут нужны в будущем

На главной странице у нас 3 вкладки, по описанию не трудно догадаться для чего каждая из них

Во вкладке `Посмотреть` можно найти все знаки, которые есть на сайте. Для удобавста есть фильтр по категориями, при нажатии на знак выводится польная информация и появляется возможность посмотртеь его вблизи

Во вкладке `Тест` можно тренироваться в ответе на вопросы, каждый раз знаки выдаются в случайном порядке, ответы показываются сразу

Во вкладке `Экзамен` вам выдается часть вопросов, ответы не показываются, результат идет в личный кабинет и ведомость, присутствует таймер

Перейдем в личный кабинет, нажав на соответсвующую иконку справа-сверху

Здесь мы видим последние 10 результатов экзамена и может заполнить поля о себе (чтобы вас смогли найти в ведомости)

___

___

## Прочее
___

<a name="7"></a>

### Планы 📈

![image](https://github.com/Nikkri20/StudySignsProject/assets/114663524/78c1c415-be2e-4423-8bc5-024f1b44bcea)
