![foodgram_workflow](https://github.com/vkorey/foodgram-project-react/actions/workflows/main.yml/badge.svg?branch=master)

# Foodgram - Продуктовый помощник
Foodgram - сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов.
Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone https://github.com/vkorey/foodgram-project-react
```
### Перейти в папку с проектом:
```
cd foodgram-project-react
```
### В папке **backend** создать файл .env с содержимым переменных окружения:

```
DB_ENGINE=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
```

### Перейти в папку **infra** и соберите docker-compose:
```
sudo docker-compose up -d --build
```
### После сборки на сервере выполните команды:
#### Соберите статические файлы:
```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```
#### Применитe миграции:
```
sudo docker-compose exec backend python manage.py migrate --noinput
```
#### Загрузите ингридиенты в базу данных (не обязательно)
```
sudo docker-compose exec backend python manage.py loaddata fixtures/fixtures.json
```
#### Создать суперпользователя Django:
```
sudo docker-compose exec backend python manage.py createsuperuser
```
Останавить и удалить контейнеры:
```
docker-compose down -v
```

## Проект доступен по адресу http://178.154.227.231
Логин:vk@vk.vk
Почта:GhbdtnGjrf

### Автор
* **Владимир Корельский** - https://github.com/vkorey
