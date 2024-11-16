# DRF_HW
Create DRF SPA Web-app. Develop LMS-system

*Запустить докер
docker run -p 8080:80 nginx:latest

*Задать настройки приложения в docker-compose.yaml

*Создать образ
docker-compose build

*Запуск конфигураций
docker-compose up -d

*Применение миграций
codker-compose exec app python manage.py migrate
