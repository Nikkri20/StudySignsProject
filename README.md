## Cайт для изучения студентами условных топографических знаков

![изображение](https://github.com/user-attachments/assets/b1953146-e135-4fbb-8b6a-a942328dac7c)

___
## Команда 🤝

### Backend-разработчик: Крылов Никита Андреевич 🛠️
### Frontend-разработчик: Карболин Сергей Александрович 🖥️
### Дизайнер: Стратюк Лада Александровна 🖌️

___

> [!NOTE]
> Данная документация по проекту была написана Backend-разработчиком (упор делается на техническую часть)

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
* [Как развернуть проект](#5) ⬇️
* [Про базы данных](#6) 🗄
* 
___

## Общая информация
___

<a name="1"></a>

### Для кого это 👥
* Для тех, кто будет продолжать данный проект (eсли кто-то будет)
* Для интересующихся
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
[![StudySignsProject Tech Stack](https://github-readme-tech-stack.vercel.app/api/cards?title=StudySignsProject+Tech+Stack&lineCount=4&line1=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPCEtLSBpY29uNjY2LmNvbSAtIE1JTExJT05TIHZlY3RvciBJQ09OUyBGUkVFIC0tPjxzdmcgdmlld0JveD0iLTMwIDAgNTEyIDUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtMCAwIDMxLjgwMDc4MSA0NDguMTAxNTYyIDE5NC4zOTg0MzggNjMuODk4NDM4IDE5NC4zOTg0MzctNjMuODk4NDM4IDMxLjgwMDc4Mi00NDguMTAxNTYyem0wIDAiIGZpbGw9IiNmZjc4MTYiPjwvcGF0aD48cGF0aCBkPSJtNDUyLjM5ODQzOCAwLTMxLjgwMDc4MiA0NDguMTAxNTYyLTE5NC4zOTg0MzcgNjMuODk4NDM4di01MTJ6bTAgMCIgZmlsbD0iI2ZmNGIwMCI%2BPC9wYXRoPjxwYXRoIGQ9Im0zNjcuNSAxMzZoLTIyMi4zMDA3ODFsNS4zOTg0MzcgNzVoMjExLjUwMzkwNmwtMTIuOTAyMzQzIDE4MS41OTc2NTYtMTIzIDQxLjEwMTU2My0xMjMtNDEuMTAxNTYzLTQuMTk5MjE5LTYwLjU5NzY1Nmg2MGwxLjE5OTIxOSAxNi41IDY2IDIxLjg5ODQzOCA2Ni0yMS44OTg0MzggNS4zOTg0MzctNzcuNWgtMjAzLjA5NzY1NmwtMTMuODAwNzgxLTE5NWgyOTF6bTAgMCIgZmlsbD0iI2VjZWNmMSI%2BPC9wYXRoPjxnIGZpbGw9IiNlMmUyZTciPjxwYXRoIGQ9Im0zNjIuMTAxNTYyIDIxMS0xMi45MDIzNDMgMTgxLjU5NzY1Ni0xMjMgNDEuMTAxNTYzdi02My4zMDA3ODFsNjYtMjEuODk4NDM4IDUuMzk4NDM3LTc3LjVoLTcxLjM5ODQzN3YtNjB6bTAgMCI%2BPC9wYXRoPjxwYXRoIGQ9Im0zNzEuNjk5MjE5IDc2LTQuMTk5MjE5IDYwaC0xNDEuMzAwNzgxdi02MHptMCAwIj48L3BhdGg%2BPC9nPjwvc3ZnPg%3D%3D%2Chtml%2C%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4IiBpZD0iY3NzMyI%2BCiAgPHBhdGggZmlsbD0iIzE1NzJCNiIgZD0iTTE4LjgxNCAxMTQuMTIzbC0xMC4wNTQtMTEyLjc3MWgxMTAuNDhsLTEwLjA2NCAxMTIuNzU0LTQ1LjI0MyAxMi41NDMtNDUuMTE5LTEyLjUyNnoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjMzNBOURDIiBkPSJNNjQuMDAxIDExNy4wNjJsMzYuNTU5LTEwLjEzNiA4LjYwMS05Ni4zNTRoLTQ1LjE2djEwNi40OXoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjZmZmIiBkPSJNNjQuMDAxIDUxLjQyOWgxOC4zMDJsMS4yNjQtMTQuMTYzaC0xOS41NjZ2LTEzLjgzMWgzNC42ODE5OTk5OTk5OTk5OTVsLS4zMzIgMy43MTEtMy40IDM4LjExNGgtMzAuOTV2LTEzLjgzMXoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjRUJFQkVCIiBkPSJNNjQuMDgzIDg3LjM0OWwtLjA2MS4wMTgtMTUuNDAzLTQuMTU5LS45ODUtMTEuMDMxaC0xMy44ODJsMS45MzcgMjEuNzE3IDI4LjMzMSA3Ljg2My4wNjMtLjAxOHYtMTQuMzl6Ij48L3BhdGg%2BCiAgPHBhdGggZmlsbD0iI2ZmZiIgZD0iTTgxLjEyNyA2NC42NzVsLTEuNjY2IDE4LjUyMi0xNS40MjYgNC4xNjR2MTQuMzlsMjguMzU0LTcuODU4LjIwOC0yLjMzNyAyLjQwNi0yNi44ODFoLTEzLjg3NnoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjRUJFQkVCIiBkPSJNNjQuMDQ4IDIzLjQzNXYxMy44MzEwMDAwMDAwMDAwMDFoLTMzLjQwNzk5OTk5OTk5OTk5NGwtLjI3Ny0zLjEwOC0uNjMtNy4wMTItLjMzMS0zLjcxMWgzNC42NDZ6TTY0LjAwMSA1MS40MzF2MTMuODMxMDAwMDAwMDAwMDAxaC0xNS4yMDlsLS4yNzctMy4xMDgtLjYzMS03LjAxMi0uMzMtMy43MTFoMTYuNDQ3eiI%2BPC9wYXRoPgo8L3N2Zz4K%2Ccss%2C%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAwIiBoZWlnaHQ9IjI1MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaW5ZTWluIG1lZXQiIHZpZXdCb3g9IjAgMCAyNTYgMjU2IiBpZD0iamF2YXNjcmlwdCI%2BCiAgPHBhdGggZmlsbD0iI0Y3REYxRSIgZD0iTTAgMGgyNTZ2MjU2SDBWMHoiPjwvcGF0aD4KICA8cGF0aCBkPSJNNjcuMzEyIDIxMy45MzJsMTkuNTktMTEuODU2YzMuNzggNi43MDEgNy4yMTggMTIuMzcxIDE1LjQ2NSAxMi4zNzEgNy45MDUgMCAxMi44OS0zLjA5MiAxMi44OS0xNS4xMnYtODEuNzk4aDI0LjA1N3Y4Mi4xMzhjMCAyNC45MTctMTQuNjA2IDM2LjI1OS0zNS45MTYgMzYuMjU5LTE5LjI0NSAwLTMwLjQxNi05Ljk2Ny0zNi4wODctMjEuOTk2TTE1Mi4zODEgMjExLjM1NGwxOS41ODgtMTEuMzQxYzUuMTU3IDguNDIxIDExLjg1OSAxNC42MDcgMjMuNzE1IDE0LjYwNyA5Ljk2OSAwIDE2LjMyNS00Ljk4NCAxNi4zMjUtMTEuODU4IDAtOC4yNDgtNi41My0xMS4xNy0xNy41MjgtMTUuOThsLTYuMDEzLTIuNThjLTE3LjM1Ny03LjM4Ny0yOC44Ny0xNi42NjctMjguODctMzYuMjU3IDAtMTguMDQ0IDEzLjc0Ny0zMS43OTIgMzUuMjI4LTMxLjc5MiAxNS4yOTQgMCAyNi4yOTIgNS4zMjggMzQuMTk2IDE5LjI0N0wyMTAuMjkgMTQ3LjQzYy00LjEyNS03LjM4OS04LjU5MS0xMC4zMS0xNS40NjUtMTAuMzEtNy4wNDYgMC0xMS41MTQgNC40NjgtMTEuNTE0IDEwLjMxIDAgNy4yMTcgNC40NjggMTAuMTQgMTQuNzc4IDE0LjYwOGw2LjAxNCAyLjU3N2MyMC40NSA4Ljc2NSAzMS45NjMgMTcuNyAzMS45NjMgMzcuODA0IDAgMjEuNjU0LTE3LjAxMiAzMy41MS0zOS44NjcgMzMuNTEtMjIuMzM5IDAtMzYuNzc0LTEwLjY1NC00My44MTktMjQuNTc0Ij48L3BhdGg%2BCjwvc3ZnPgo%3D%2Cjavascript%2C%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4IiBpZD0ibm9kZS1qcyI%2BCiAgPHBhdGggZmlsbD0iIzgzQ0QyOSIgZD0iTTExMi43NzEgMzAuMzM0bC00NC4wOTctMjUuNjA1Yy0yLjc4MS0xLjU4NC02LjQwMi0xLjU4NC05LjIwNSAwbC00NC41NjggMjUuNjA1Yy0yLjg3IDEuNjUxLTQuOTAxIDQuNzU0LTQuOTAxIDguMDczdjUxLjE0MmMwIDMuMzE5IDIuMDg0IDYuNDIzIDQuOTU0IDguMDgzbDExLjc3NSA2LjY4OGM1LjYyOCAyLjc3MiA3LjYxNyAyLjc3MiAxMC4xNzggMi43NzIgOC4zMzMgMCAxMy4wOTMtNS4wMzkgMTMuMDkzLTEzLjgyOHYtNTAuNDljMC0uNzEzLS4zNzEtMS43NzQtMS4wNzEtMS43NzRoLTUuNjIzYy0uNzEyIDAtMi4zMDYgMS4wNjEtMi4zMDYgMS43NzN2NTAuNDljMCAzLjg5Ni0zLjUyNCA3Ljc3My0xMC4xMSA0LjQ4bC0xMi4xNjctNy4wMTNjLS40MjQtLjIzLS43MjMtLjY5My0uNzIzLTEuMTgxdi01MS4xNDJjMC0uNDgyLjU1NS0uOTY2Ljk4Mi0xLjIxM2w0NC40MjQtMjUuNTYxYy40MTUtLjIzNSAxLjAyNS0uMjM1IDEuNDM5IDBsNDMuODgyIDI1LjU1NWMuNDIuMjUzLjI3Mi43MjIuMjcyIDEuMjE5djUxLjE0MmMwIC40ODguMTgzLjk2My0uMjMyIDEuMTk4bC00NC4wODYgMjUuNTc2Yy0uMzc4LjIyNy0uODQ3LjIyNy0xLjI2MSAwbC0xMS4zMDctNi43NDljLS4zNDEtLjE5OC0uNzQ2LS4yNjktMS4wNzMtLjA4Ni0zLjE0NiAxLjc4My0zLjcyNiAyLjAyLTYuNjc3IDMuMDQzLS43MjYuMjUzLTEuNzk3LjY5Mi40MSAxLjkyOWwxNC43OTggOC43NTRjMS40MTcuODIgMy4wMjcgMS4yNDYgNC42NDcgMS4yNDYgMS42NDIgMCAzLjI1LS40MjYgNC42NjctMS4yNDZsNDMuODg1LTI1LjU4MmMyLjg3LTEuNjcyIDQuMjMtNC43NjQgNC4yMy04LjA4M3YtNTEuMTQyYzAtMy4zMTktMS4zNi02LjQxNC00LjIyOS04LjA3M3pNNzcuOTEgODEuNDQ1Yy0xMS43MjYgMC0xNC4zMDktMy4yMzUtMTUuMTctOS4wNjYtLjEtLjYyOC0uNjMzLTEuMzc5LTEuMjcyLTEuMzc5aC01LjczMWMtLjcwOSAwLTEuMjc5Ljg2LTEuMjc5IDEuNTY2IDAgNy40NjYgNC4wNTkgMTYuNTEyIDIzLjQ1MyAxNi41MTIgMTQuMDM5IDAgMjIuMDg4LTUuNDU1IDIyLjA4OC0xNS4xMDkgMC05LjU3Mi02LjQ2Ny0xMi4wODQtMjAuMDgyLTEzLjg4Ni0xMy43NjItMS44MTktMTUuMTYtMi43MzgtMTUuMTYtNS45NjIgMC0yLjY1OCAxLjE4NC02LjIwMyAxMS4zNzQtNi4yMDMgOS4xMDUgMCAxMi40NjEgMS45NTQgMTMuODQyIDguMDkxLjExOC41NzcuNjQ1Ljk5MSAxLjI0Ljk5MWg1Ljc1NGMuMzU0IDAgLjY5Mi0uMTQzLjk0LS4zOTYuMjQtLjI3Mi4zNjctLjYxMy4zMzUtLjk3OS0uODkxLTEwLjU2OC03LjkxMi0xNS40OTMtMjIuMTEyLTE1LjQ5My0xMi42MzEgMC0yMC4xNjYgNS4zMzQtMjAuMTY2IDE0LjI3NSAwIDkuNjk4IDcuNDk3IDEyLjM3OCAxOS42MjIgMTMuNTc3IDE0LjUwNSAxLjQyMiAxNS42MzMgMy41NDIgMTUuNjMzIDYuMzk1IDAgNC45NTUtMy45NzggNy4wNjYtMTMuMzA5IDcuMDY2eiI%2BPC9wYXRoPgo8L3N2Zz4K%2Cnode.js%2C%3B&line2=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIGlkPSJmaWdtYSI%2BCiAgPHBhdGggZmlsbD0iIzBBQ0Y4MyIgZD0iTTgsMjRjMi4yMDgsMCw0LTEuNzkyLDQtNHYtNEg4Yy0yLjIwOCwwLTQsMS43OTItNCw0QzQsMjIuMjA4LDUuNzkyLDI0LDgsMjRMOCwyNHoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjQTI1OUZGIiBkPSJNNCwxMmMwLTIuMjA4LDEuNzkyLTQsNC00aDR2OEg4QzUuNzkyLDE2LDQsMTQuMjA4LDQsMTJMNCwxMnoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjRjI0RTFFIiBkPSJNNCw0YzAtMi4yMDgsMS43OTItNCw0LTRoNHY4SDhDNS43OTIsOCw0LDYuMjA4LDQsNEw0LDR6Ij48L3BhdGg%2BCiAgPHBhdGggZmlsbD0iIzA5QjQ3MiIgZD0iTTguNDE5LDE2SDhjLTIuMjA4LDAtNCwxLjc5Mi00LDRjMCwyLjIwOCwxLjc5Miw0LDQsNGwwLDBjMC4xNDIsMCwwLjI4MS0wLjAwNywwLjQxOS0wLjAyMlYxNkw4LjQxOSwxNnoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjOEQ0RERFIiBkPSJNOC40MTksOEg4Yy0yLjIwOCwwLTQsMS43OTItNCw0czEuNzkyLDQsNCw0aDAuNDE5VjhMOC40MTksOHoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjRDM0NDFBIiBkPSJNOC40MTksMEg4QzUuNzkyLDAsNCwxLjc5Miw0LDRzMS43OTIsNCw0LDRoMC40MTlWMEw4LjQxOSwweiI%2BPC9wYXRoPgogIDxwYXRoIGZpbGw9IiNGRjcyNjIiIGQ9Ik0xMiwwaDRjMi4yMDgsMCw0LDEuNzkyLDQsNGMwLDIuMjA4LTEuNzkyLDQtNCw0aC00VjBMMTIsMHoiPjwvcGF0aD4KICA8cGF0aCBmaWxsPSIjMUFCQ0ZFIiBkPSJNMjAsMTJjMCwyLjIwOC0xLjc5Miw0LTQsNGMtMi4yMDgsMC00LTEuNzkyLTQtNGMwLTIuMjA4LDEuNzkyLTQsNC00QzE4LjIwOCw4LDIwLDkuNzkyLDIwLDEyTDIwLDEyeiI%2BPC9wYXRoPgogIDxwb2x5Z29uIGZpbGw9IiNERTYzNTUiIHBvaW50cz0iMTYgMCAxMiAwIDEyIDggMTYgOCAxNiA4IDE2IDggMTYgMCAxNiAwIj48L3BvbHlnb24%2BCiAgPHBhdGggZmlsbD0iIzE3QTRERCIgZD0iTTE2LDhMMTYsOGMtMi4yMDgsMC00LDEuNzkyLTQsNGMwLDIuMjA4LDEuNzkyLDQsNCw0bDAsMFY4TDE2LDhMMTYsOHoiPjwvcGF0aD4KPC9zdmc%2BCg%3D%3D%2Cfigma%2C%3B&line3=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNTAwIiBoZWlnaHQ9IjI0OTAiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaW5ZTWluIG1lZXQiIHZpZXdCb3g9IjAgMCAyNTYgMjU1IiBpZD0icHl0aG9uIj4KICA8ZGVmcz4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYSIgeDE9IjEyLjk1OSUiIHgyPSI3OS42MzklIiB5MT0iMTIuMDM5JSIgeTI9Ijc4LjIwMSUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjMzg3RUI4Ij48L3N0b3A%2BCiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iIzM2Njk5NCI%2BPC9zdG9wPgogICAgPC9saW5lYXJHcmFkaWVudD4KICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYiIgeDE9IjE5LjEyOCUiIHgyPSI5MC43NDIlIiB5MT0iMjAuNTc5JSIgeTI9Ijg4LjQyOSUiPgogICAgICA8c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSIjRkZFMDUyIj48L3N0b3A%2BCiAgICAgIDxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iI0ZGQzMzMSI%2BPC9zdG9wPgogICAgPC9saW5lYXJHcmFkaWVudD4KICA8L2RlZnM%2BCiAgPHBhdGggZmlsbD0idXJsKCNhKSIgZD0iTTEyNi45MTYuMDcyYy02NC44MzIgMC02MC43ODQgMjguMTE1LTYwLjc4NCAyOC4xMTVsLjA3MiAyOS4xMjhoNjEuODY4djguNzQ1SDQxLjYzMVMuMTQ1IDYxLjM1NS4xNDUgMTI2Ljc3YzAgNjUuNDE3IDM2LjIxIDYzLjA5NyAzNi4yMSA2My4wOTdoMjEuNjF2LTMwLjM1NnMtMS4xNjUtMzYuMjEgMzUuNjMyLTM2LjIxaDYxLjM2MnMzNC40NzUuNTU3IDM0LjQ3NS0zMy4zMTlWMzMuOTdTMTk0LjY3LjA3MiAxMjYuOTE2LjA3MnpNOTIuODAyIDE5LjY2YTExLjEyIDExLjEyIDAgMCAxIDExLjEzIDExLjEzIDExLjEyIDExLjEyIDAgMCAxLTExLjEzIDExLjEzIDExLjEyIDExLjEyIDAgMCAxLTExLjEzLTExLjEzIDExLjEyIDExLjEyIDAgMCAxIDExLjEzLTExLjEzeiI%2BPC9wYXRoPgogIDxwYXRoIGZpbGw9InVybCgjYikiIGQ9Ik0xMjguNzU3IDI1NC4xMjZjNjQuODMyIDAgNjAuNzg0LTI4LjExNSA2MC43ODQtMjguMTE1bC0uMDcyLTI5LjEyN0gxMjcuNnYtOC43NDVoODYuNDQxczQxLjQ4NiA0LjcwNSA0MS40ODYtNjAuNzEyYzAtNjUuNDE2LTM2LjIxLTYzLjA5Ni0zNi4yMS02My4wOTZoLTIxLjYxdjMwLjM1NXMxLjE2NSAzNi4yMS0zNS42MzIgMzYuMjFoLTYxLjM2MnMtMzQuNDc1LS41NTctMzQuNDc1IDMzLjMydjU2LjAxM3MtNS4yMzUgMzMuODk3IDYyLjUxOCAzMy44OTd6bTM0LjExNC0xOS41ODZhMTEuMTIgMTEuMTIgMCAwIDEtMTEuMTMtMTEuMTMgMTEuMTIgMTEuMTIgMCAwIDEgMTEuMTMtMTEuMTMxIDExLjEyIDExLjEyIDAgMCAxIDExLjEzIDExLjEzIDExLjEyIDExLjEyIDAgMCAxLTExLjEzIDExLjEzeiI%2BPC9wYXRoPgo8L3N2Zz4K%2Cpython%2C%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxOTYzIiBoZWlnaHQ9IjI1MDAiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaW5ZTWluIG1lZXQiIHZpZXdCb3g9IjAgMCAyNTYgMzI2IiBpZD0iZGphbmdvIj4KICA8ZyBmaWxsPSIjMkJBOTc3Ij4KICAgIDxwYXRoIGQ9Ik0xMTQuNzg0IDBoNTMuMjc4djI0NC4xOTFjLTI3LjI5IDUuMTYyLTQ3LjM4IDcuMTkzLTY5LjExNyA3LjE5M0MzMy44NzMgMjUxLjMxNiAwIDIyMi4yNDUgMCAxNjYuNDEyYzAtNTMuNzk1IDM1LjkzLTg4LjcwOCA5MS42MDgtODguNzA4IDguNjQgMCAxNS4yMjIuNjggMjMuMTc2IDIuNzE3VjB6bTEuODY3IDEyNC40MjdjLTYuMjQtMi4wMzgtMTEuMzgyLTIuNzE3LTE3Ljk2NS0yLjcxNy0yNi45NDcgMC00Mi41MTIgMTYuNDM3LTQyLjUxMiA0NS4yNDMgMCAyOC4wNDYgMTQuODggNDMuNTMyIDQyLjE3IDQzLjUzMiA1Ljg5NiAwIDEwLjY5Ni0uMzMyIDE4LjMwNy0xLjM1MXYtODQuNzA3eiI%2BPC9wYXRoPgogICAgPHBhdGggZD0iTTI1NS4xODcgODQuMjZ2MTIyLjI2M2MwIDQyLjEwNS0zLjE1NCA2Mi4zNTMtMTIuNDExIDc5LjgxLTguNjQgMTYuNzgzLTIwLjAyMiAyNy4zNjYtNDMuNTQxIDM5LjA1NWwtNDkuNDM4LTIzLjI5N2MyMy41MTktMTAuOTMgMzQuOTAxLTIwLjU4OCA0Mi4xNy0zNS4zMjcgNy42MS0xNS4wNzIgMTAuMDEtMzIuNTI5IDEwLjAxLTc4LjQ0NVY4NC4yNjFoNTMuMjF6TTE5Ni42MDggMGg1My4yNzh2NTQuMTM1aC01My4yNzhWMHoiPjwvcGF0aD4KICA8L2c%2BCjwvc3ZnPgo%3D%2Cdjango%2C%3B&line4=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4IiBpZD0idWJ1bnR1Ij4KICA8cGF0aCBmaWxsPSIjREQ0ODE0IiBkPSJNNjQgMy4yNDZjLTMzLjU1NSAwLTYwLjc1NSAyNy4yLTYwLjc1NSA2MC43NTQgMCAzMy41NTIgMjcuMiA2MC43NTQgNjAuNzU1IDYwLjc1NCAzMy41NTQgMCA2MC43NTUtMjcuMjAyIDYwLjc1NS02MC43NTQgMC0zMy41NTQtMjcuMi02MC43NTQtNjAuNzU1LTYwLjc1NHptMTMuNjMxIDIwLjkyMmMyLjI0Mi0zLjg4MSA3LjItNS4yMSAxMS4wOC0yLjk3MiAzLjg4IDIuMjQyIDUuMjA4IDcuMiAyLjk2NiAxMS4wOC0yLjIzOCAzLjg4LTcuMTk3IDUuMjA4LTExLjA3NyAyLjk2Ny0zLjg3Ny0yLjIzOS01LjIwNi03LjE5OC0yLjk2OS0xMS4wNzV6bS0xMy42MzEgNC41OTVjMy4yNjIgMCA2LjQxNy40NTMgOS40MTQgMS4yODEuNTI5IDMuMjU5IDIuNDYzIDYuMjYyIDUuNTQ4IDguMDQyIDMuMDc5IDEuNzc1IDYuNjQyIDEuOTUzIDkuNzI1Ljc4OSA1Ljk5OCA1Ljg5OCA5LjkwMSAxMy45MTkgMTAuNDcgMjIuODU0bC0xMS41NTguMTdjLTEuMDY3LTEyLjEwMy0xMS4yMjItMjEuNTkzLTIzLjU5OS0yMS41OTMtMy41NjUgMC02Ljk0OC43OTItOS45OCAyLjIwM2wtNS42MzctMTAuMDk5YzQuNzA4LTIuMzMgMTAuMDEtMy42NDcgMTUuNjE3LTMuNjQ3em0tNDEuMzExIDQzLjM0OWMtNC40ODIgMC04LjExMy0zLjYzMi04LjExMy04LjExMiAwLTQuNDgxIDMuNjMtOC4xMTMgOC4xMTMtOC4xMTMgNC40NzkgMCA4LjExMSAzLjYzMSA4LjExMSA4LjExMyAwIDQuNDc5LTMuNjMyIDguMTEyLTguMTExIDguMTEyem03LjE5MS43MjJjMi41NjEtMi4wOSA0LjItNS4yNzEgNC4yLTguODM0IDAtMy41NjUtMS42MzktNi43NDctNC4yLTguODM2IDIuMTk0LTguNDg5IDcuNDc1LTE1LjczOCAxNC41NzEtMjAuNDgzbDUuOTMxIDkuOTM0Yy02LjA5MiA0LjI4Ny0xMC4wNzQgMTEuMzY5LTEwLjA3NCAxOS4zODVzMy45ODEgMTUuMDk4IDEwLjA3NCAxOS4zODNsLTUuOTMxIDkuOTM3Yy03LjA5OS00Ljc0NC0xMi4zOC0xMS45OTUtMTQuNTcxLTIwLjQ4NnptNTguODMxIDMzLjk2NGMtMy44NzkgMi4yNDEtOC44MzguOTEyLTExLjA3Ny0yLjk2OS0yLjI0MS0zLjg3Ny0uOTExLTguODM1IDIuOTY5LTExLjA3NiAzLjg3Ny0yLjIzOSA4LjgzOC0uOTA4IDExLjA3NyAyLjk2OSAyLjI0IDMuODguOTEgOC44MzktMi45NjkgMTEuMDc2em0tLjAyNC0xNy42NzNjLTMuMDgzLTEuMTY2LTYuNjQ1LS45OTEtOS43MjUuNzg4LTMuMDg0IDEuNzgzLTUuMDE5IDQuNzgyLTUuNTQ3IDguMDQyLTIuOTk4LjgzLTYuMTUzIDEuMjg0LTkuNDE1IDEuMjg0LTUuNjA3IDAtMTAuOTA5LTEuMzE4LTE1LjYxNi0zLjY0OWw1LjYzNi0xMC4xYzMuMDMyIDEuNDExIDYuNDE1IDIuMjA0IDkuOTggMi4yMDQgMTIuMzc4IDAgMjIuNTMyLTkuNDg4IDIzLjU5Ni0yMS41OTJsMTEuNTYxLjE2OWMtLjU2OSA4LjkzNS00LjQ3MiAxNi45NTYtMTAuNDcgMjIuODU0eiI%2BPC9wYXRoPgo8L3N2Zz4K%2Cubuntu%2C%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTIwIiBoZWlnaHQ9IjEyMCIgdmlld0JveD0iMCAwIDEyMCAxMjAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI%2BCjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMF8yNDg4XzcwNDMpIj4KPHBhdGggZD0iTTIwIDYwQzIwIDM3LjkwODYgMzcuOTA4NiAyMCA2MCAyMFYyMEM4Mi4wOTE0IDIwIDEwMCAzNy45MDg2IDEwMCA2MFY2MEMxMDAgODIuMDkxNCA4Mi4wOTE0IDEwMCA2MCAxMDBWMTAwQzM3LjkwODYgMTAwIDIwIDgyLjA5MTQgMjAgNjBWNjBaIiBmaWxsPSJ3aGl0ZSIvPgo8cGF0aCBkPSJNNTkuOTk5OCAxMjBDNDUuMDg5OSAxMTkuNjQgMzkuMTg3NyAxMDkuNjczIDM3LjM4NjEgMTAwLjA0N0MzNi40MDgyIDk0LjgxNDQgMzYuODM3MSA4Ni4xMTM4IDM3LjM4NjEgODMuMDA4M0MzOC4yNzgzIDc3Ljk0NjggMzkuNzE5NiA3MC42NzIgNDEuMzE1MiA2Mi4yMzA1QzQzLjU5NzIgNTAuMTM0NCA0OS42NTM4IDQzLjI1NDIgNjIuNzI3OSA0MC44MDA3TDg0LjExMzIgMzYuNzE2N0M4NC42Nzk0IDMzLjU0MjUgODUuNzUzMyAyNS4xMzU4IDg0Ljc3NTMgMTkuOTU0MkM4Mi45NTY2IDEwLjIyNTkgNzUuNDU4OCAwLjE1NDQxOSA2MC4yNCAyLjE3OTUzZS0wNkMyNy4wOTE2IDUuMDc3NDVlLTA2IC0wLjAwMDIxNDEzNyAyNi44NTE2IC0wLjAwMDIxMTIzOSA2MEMtMC4wMDAyMDgzNDEgOTMuMTQ4NCAyNi44NTE0IDEyMCA1OS45OTk4IDEyMFoiIGZpbGw9IiM5RUI5RkYiLz4KPHBhdGggZD0iTTU5Ljk5OTggMEM3NC45MDk3IDAuMzYwMzA5IDgyLjI4NzQgMTAuMzQ2IDg0LjA4OSAxOS45NzE0Qzg1LjA2NyAyNS4yMDQ1IDgzLjE2MjUgMzMuODg2MiA4Mi42MTM0IDM2Ljk5MTdDODEuNzIxMiA0Mi4wNTMyIDgwLjI4IDQ5LjMyOCA3OC42ODQzIDU3Ljc2OTVDNzYuNDAyNCA2OS44NjU2IDcwLjM0NTggNzYuNzQ1OCA1Ny4yNzE3IDc5LjE5OTNMMzcuMzcwOSA4My4xMDY2QzM2LjgwNDcgODYuMjgwNyAzNC45MzQ1IDk0Ljg1OTUgMzUuOTEyNSAxMDAuMDQxQzM3LjczMTIgMTA5Ljc2OSA0NC41NDA4IDExOS44NDYgNTkuNzU5NiAxMjBDOTIuOTA4IDEyMCAxMjAgOTMuMTQ4NCAxMjAgNjBDMTIwIDI2Ljg1MTYgOTMuMTQ4MiAwIDU5Ljk5OTggMFoiIGZpbGw9IiM1MjgyRkYiLz4KPC9nPgo8ZGVmcz4KPGNsaXBQYXRoIGlkPSJjbGlwMF8yNDg4XzcwNDMiPgo8cmVjdCB3aWR0aD0iMTIwIiBoZWlnaHQ9IjEyMCIgZmlsbD0id2hpdGUiLz4KPC9jbGlwUGF0aD4KPC9kZWZzPgo8L3N2Zz4K%2Cyandex+cloud%2C%3Bdata%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB2aWV3Qm94PSIwIDAgNDggNDgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjI1MDAiIGhlaWdodD0iMjUwMCI%2BPHBhdGggZD0iTTAgMGg0OHY0OEgweiIgZmlsbD0iI2ZmZDAyZiIvPjxwYXRoIGQ9Ik0zMi43MDggNi40aC01LjEyNGw0LjU0OSA3LjA1LTkuNjE3LTcuMDVoLTUuMTI0bDQuNTQ5IDkuMjM4TDEyLjMyNCA2LjRINy4ybDQuNDc0IDExLjkyNkw3LjIgNDEuNmg1LjEyNGw5LjYxNy0yNC45NTVMMTcuMzkyIDQxLjZoNS4xMjRsOS42MTctMjcuMTQyLTQuNTQ5IDI3LjE0Mmg1LjEyNEw0Mi40IDExLjc4NXoiIGZpbGw9IiMwNTAwMzgiLz48L3N2Zz4%3D%2Cmiro%2C%3B)

[К оглавлению](#0) ⬆️
___

## Для разработчиков
___

<a name="4"></a>

### Структура проекта 🗂️

> [!NOTE]
> Кратко описал предназначение каждого элемента для быстрого вкатывания в проект, для более подробной и точной информации лучше ознакомиться с официальной документацией Django: https://docs.djangoproject.com/en/5.0/ 


[К оглавлению](#0) ⬆️
___

<a name="5"></a>

### Как развернуть проект ⬇️

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

3. (Необязательно) Создаем .venv (чтобы не засорять вашу систему нашими зависимостями. При удалении проекта удалятся и все зависимости, которые мы установим далее)

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

[К оглавлению](#0) ⬆️
___
