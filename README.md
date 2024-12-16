# Сервис по работе с курсами и лекциями
Create DRF SPA Web-app. Develop LMS-system
***
1. Запустить докер

* `docker run -p 8080:80 nginx:latest`

2. Задать настройки приложения в `docker-compose.yaml`

3. Создать образ

* `docker-compose build`

4. Запуск конфигураций

* `docker-compose up -d`

5. Применение миграций

* `docker-compose exec app python manage.py migrate`
