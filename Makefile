
.PHONY: dev
dev:
	poetry install
	poetry run pre-commit install

.PHONY: test
test:
	poetry run tox

.PHONY: black
black:
	poetry run black .
