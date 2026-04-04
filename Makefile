manage := python manage.py

.PHONY: run
run:
	${manage} runserver

.PHONY: migrations apply-migrations
migrations:
	${manage} makemigrations
apply-migrations:
	${manage} migrate
