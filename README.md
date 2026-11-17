# Docker Application — Yandex Cloud

## Описание

Тестовое Flask-приложение для дипломного проекта «Базовая DevOps-инфраструктура в Yandex Cloud».

Приложение упаковано в Docker-контейнер, а его автоматическая сборка, публикация и развёртывание выполняются через GitHub Actions.

## Структура проекта

```text
docker-app-yandex-cloud/
├── .github/workflows/
│   └── deploy.yml
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .dockerignore
```

## Используемые технологии

- Python и Flask
- Docker
- Docker Compose
- Docker Hub
- GitHub Actions

## Проверка приложения

Главная страница: `http://IP-АДРЕС-ВМ:8081/`

Проверка состояния: `http://IP-АДРЕС-ВМ:8081/health`

## Docker Hub

[Опубликованный Docker-образ](https://hub.docker.com/r/kumarina/docker-app-yandex-cloud)

## CI/CD

При push в ветку `main` GitHub Actions автоматически собирает Docker-образ, публикует его в Docker Hub и обновляет контейнер на виртуальной машине в Yandex Cloud.

## Связанные проекты

- [Terraform — инфраструктура](https://github.com/kumarina-max/terraform-yandex-cloud)
- [Ansible — настройка ВМ](https://github.com/kumarina-max/ansible-yandex-cloud)
