# web_project_LMS
SPA веб-приложение
бэкенд-сервер, который возвращает клиенту JSON-структуры

1.
# Сборка образов
docker-compose build

2.
# Запуск контейнеров
docker-compose up

3.
# Запуск контейнеров в фоне
docker-compose up -d

4.
# Сборка образа и запуск в фоне после успешной сборки
docker-compose up -d —build

5.
# Выполнение команды <command> внутри контейнера <app>
docker-compose exec <app> <command>