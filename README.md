# Base project FastAPI + PostgreSQL
## Описание
Сервис является простым примером приложения поиска сигнатур для пациентов на FastAPI с базой данных PostgreSQL. Приложение запускается в Docker.

## Использование сервиса
Поиск пациентов осуществляется по их id на endpoint:
```
http://0.0.0.0/patients_template/{patient_id}
```

При отсутствии пациента в базе будет выведено сообщение об ошибке.

## Запуск сервиса в Docker
Для сборки контейнеров и их запуска выполнить:
```
docker compose up -d
```
Далее собираются два образа: fast_api_postgresql-dbserver и fast_api_postgresql-backend - и запускаются контейнеры с ними. В контейнере fast_api_postgresql-backend стартует приложение FastAPI, а в fast_api_postgresql-dbserver запускается база patients. В таблицу signatures в схеме content мигрировано содержимое файла signatures.csv.
