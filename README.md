# Mailing list management

## Описание проекта

Чтобы удержать текущих клиентов, часто используют вспомогательные, или «прогревающие», рассылки для информирования и привлечения клиентов.

Здесь представлен проект сервиса управления рассылками, администрирования и получения статистики.

## Технологии

- Linux
- Python
- Poetry
- Django
- PostgreSQL
- Redis
- Crontab

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Redis на компьютер командой `sudo apt install redis`
2. При необходимости установите Postfix на компьютер командой `sudo apt install postfix`
3. Cклонируйте репозиторий себе на компьютер
4. Установите необходимые зависимости командой `poetry install`
5. Создайте БД
6. Создайте файл .env и заполните его, используя образец из файла .env.example
7. Выполните миграции командой `python manage.py migrate`
8. Создайте суперпользователя командой `python manage.py csu`
9. Создайте группу Manager командой `python manage.py create_manager_group`
10. Для запуска Crontab воспользуйтесь командой `python manage.py crontab add`

## Авторы

UlianaSem

## Примеры использования

1. Регистрация пользователя
![](/readme_screen/register_1.png)
![](/readme_screen/register_2.png)
2. Экран менеджера
![](/readme_screen/manager's_screen.png)
3. Экран пользователя
![](/readme_screen/user's_screen.png)
4. Создание рассылки
![](/readme_screen/create.png)
5. Редактирование рассылки
![](/readme_screen/edit.png)
6. Просмотр логов
![](/readme_screen/log.png)

## Связь с авторами

https://github.com/UlianaSem/
