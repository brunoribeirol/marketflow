# Makefile for MarketFlow Project

# Variables
COMPOSE=docker-compose
PYTHON=$(COMPOSE) exec app python
PYTEST=$(COMPOSE) exec app pytest

# Help
.PHONY: help
help:
	@echo ""
	@echo "MarketFlow - Available Commands:"
	@echo "  make build         → Build Docker containers"
	@echo "  make up            → Start containers in detached mode"
	@echo "  make down          → Stop and remove containers and volumes"
	@echo "  make bash          → Open shell in app container"
	@echo "  make logs          → Show app container logs"
	@echo "  make run           → Run the application manually"
	@echo "  make test          → Run all tests with pytest"
	@echo "  make lint          → Lint code using flake8"
	@echo "  make format        → Format code using black"
	@echo "  make db            → Open MariaDB terminal"
	@echo ""

# Build containers
.PHONY: build
build:
	$(COMPOSE) build

# Start services
.PHONY: up
up:
	$(COMPOSE) up -d

# Stop and remove services and volumes
.PHONY: down
down:
	$(COMPOSE) down -v --remove-orphans

# Access app container shell
.PHONY: bash
bash:
	$(COMPOSE) exec app /bin/sh

# Show logs from app container
.PHONY: logs
logs:
	$(COMPOSE) logs -f app

# Run application manually
.PHONY: run
run:
	$(PYTHON) main.py

# Run tests
.PHONY: test
test:
	$(PYTEST) /app/tests -v

# Lint code using flake8
.PHONY: lint
lint:
	$(COMPOSE) exec app flake8 app

# Format code using black
.PHONY: format
format:
	$(COMPOSE) exec app black app

# Access MariaDB shell
.PHONY: db
db:
	$(COMPOSE) exec db mariadb -u user -ppass marketflow_db
