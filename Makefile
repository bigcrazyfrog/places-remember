all: makemigrations migrate run

run:
	python3 src/manage.py runserver

bot:
	python3 src/manage.py bot

build:
	docker build -t bot-app:1 .

down:
	docker compose down --remove-orphans

up:
	docker compose up -d

test:
	echo "test"

migrate:
	python3 src/manage.py migrate

makemigrations:
	python3 src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

run_prometheus_server:
	python src/manage.py runprometheusserver


createsuperuser:
	python3 src/manage.py createsuperuser

collectstatic:
	python3 src/manage.py collectstatic --no-input

dev:
	python3 src/manage.py runserver localhost:8000

command:
	python3 src/manage.py ${c}

shell:
	python3 src/manage.py shell

debug:
	python3 src/manage.py debug

piplock:
	pipenv install
	sudo chown -R ${USER} Pipfile.lock

lint:
	isort .
	flake8 --config setup.cfg

check_lint:
	isort --check --diff .
	flake8 --config setup.cfg
