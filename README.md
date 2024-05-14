# Lexicom Test Tast FastAPI 

## app - Backend Проекта
## Решение задачи №2 - в конце данного файла


# Настройка

### Настройка происходит в файле .env его нет в репозитории, т.к. он конфиденциален, но я предоставил файл .env.dist (c отладочными данными) создайте на его основе файл .env и проведите все необходимые настройки.

# Установка зависимостей

### В основе проекта лежит пакетный менеджер poetry.

`poetry install` - Вариант с использованием poetry.

# Запуск

### Для запуска воспользуйтесь ниже приведёнными командами.

`python -m app` - Команда для запуска backend'а.


# Запуск и сборка с помощью Docker

### Команда для сборки и поднятия контейнеров с приложением

`docker-compose up --build`

### Команда для остановки работы контейнеров

`docker-compose down`




#
#
#
# Решение задачи №2

## Использовать JOIN.
### Возможно использовать JOIN для объединения двух таблиц по имени файла и обновления статуса в соседней таблице

```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name = SUBSTRING(full_names.name FROM 1 FOR LENGTH(short_names.name));
```
Тут используется функция SUBSTRING - это используется для удаления расширения файлов, какая бы она не была, .mp3 .waw .kakdela и т. д.


## Использовать Подзапрсы.
### Можно использовать подзапрос для получения статуса из таблицы short_names и обновления статуса в таблице full_names

```
UPDATE full_names
SET status = (SELECT status FROM short_names WHERE short_names.name = SUBSTRING(full_names.name FROM 1 FOR POSITION('.' IN full_names.name) - 1))
WHERE POSITION('.' IN full_names.name) > 1;

```
Этот запрос использует подзапрос для получения статуса из таблицы short_names с помощью функции SUBSTRING, которая используется для удаления расширения из имени файла в таблице full_names. Затем запрос обновляет статус в таблице full_names с помощью значения статуса из подзапроса.


## Индексы.
### Можно попробовать настроить индексы на поля short_names и full_names

```
CREATE INDEX idx_short_names_name ON short_names (name);
```
Аналогично
```
CREATE INDEX idx_full_names_name ON full_names (name);
```

Есть большая вероятность что в данном случае индексы очень хорошо помогут.



