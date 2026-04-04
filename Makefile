manage := python manage.py

.PHONY: stop prune
stop:
	docker compose down --timeout 0 --remove-orphans
prune: stop
	docker system prune -a -f --volumes

.PHONY: run db
run:
	${manage} runserver
db: stop
	docker-compose up --detach

.PHONY: migrations apply-migrations
migrations:
	${manage} makemigrations
apply-migrations:
	${manage} migrate
