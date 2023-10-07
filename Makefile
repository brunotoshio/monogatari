
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

.PHONY: release-patch
release-patch:
	poetry version patch
	git tag -a "release-$(shell poetry version -s)" -m "Version $(shell poetry version -s)"
	git push --follow-tags
