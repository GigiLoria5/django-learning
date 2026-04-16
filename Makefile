manage := python manage.py

.PHONY: install stop prune
install:
	uv sync
stop:
	docker compose down --timeout 0 --remove-orphans
prune: stop
	docker system prune -a -f --volumes

.PHONY: migrations apply-migrations
migrations:
	${manage} makemigrations
apply-migrations:
	${manage} migrate

.PHONY: run db db-seeded
run:
	${manage} runserver
db: stop
	docker-compose up --detach
db-seeded: db apply-migrations

