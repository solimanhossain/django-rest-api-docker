.PHONY: runserver migrate newproject superuser

runserver: migrate
	poetry run python manage.py runserver 0.0.0.0:8000

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

newproject:
	@echo "Project Name:"
	@read PROJECT_NAME && \
	poetry run django-admin startproject $$PROJECT_NAME

superuser:
	poetry run python manage.py createsuperuser
	