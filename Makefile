include .env

BIN_DIR ?= $(shell pwd)/tmp/bin
SRC_DIR ?= ./src

USER ?= nikita
PYTHON = python3

DOCKER_DIR = .
DOCKER_FILE = $(DOCKER_DIR)/Dockerfile
DOCKER_COMPOSE_FILE = $(DOCKER_DIR)/docker-compose.yml

.PHONY: all
all: migrate up

.PHONY: run
run:
	$(PYTHON) $(SRC_DIR)/manage.py runserver $(HOST):$(PORT)

.PHONY: build
build:
	docker build -f $(DOCKER_FILE) -t $(IMAGE_NAME) .

.PHONY: down
down:
	docker compose -f $(DOCKER_COMPOSE_FILE) down --remove-orphans

.PHONY: up
up: down
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d

.PHONY: lint
lint:
	isort .
	flake8 --config setup.cfg

.PHONY: test
test:
	echo "test"

.PHONY: migrate
migrate:
	$(PYTHON) $(SRC_DIR)/manage.py migrate

.PHONY: makemigrations
makemigrations:
	$(PYTHON) $(SRC_DIR)/manage.py makemigrations
	sudo chown -R ${USER} $(SRC_DIR)/app/migrations/

.PHONY: createsuperuser
createsuperuser:
	$(PYTHON) $(SRC_DIR)/manage.py createsuperuser

.PHONY: collectstatic
collectstatic:
	$(PYTHON) $(SRC_DIR)/manage.py collectstatic --no-input

.PHONY: shell
shell:
	$(PYTHON) $(SRC_DIR)/manage.py shell

.PHONY: piplock
piplock:
	pipenv install
	sudo chown -R ${USER} Pipfile.lock

.PHONY: clean
clean:
	git clean -Xfd .
