# Тестовое задание Mailganer

## Небольшой сервис отправки email рассылок с поздравлением с днем рождения

### В проекте использовались

- python==2.7
- Django==1.11.29
- celery==4.4.7
- redis==3.5.3
- django-celery-beat==1.1.1

### Для запуска проекта:

1. Через docker:

- Нужно выполнить одну команду (будет использоваться postgresql).

```shell
docker compose up --build -d
```

2. Вручную (sqlite3)

- Установка зависимостей из reqirements.txt

```shell
pip install -r requirements.txt
```

- Применение миграций и запуск приложения

```shell
python ./manage.py migrate
python ./manage.py runserver
```

- запуск redis

```shell
docker compose up -d redis
```

- запуск beat сервис

```shell
celery -A serve_mail beat -l info -S django
```

- запуск воркера

```shell
celery -A serve_mail worker --loglevel=info
```



