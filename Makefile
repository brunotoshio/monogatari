
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
release-patch: test
	poetry run bump2version patch
	git push --follow-tags

.PHONY: release-minor
release-minor: test
	poetry run bump2version minor
	git push --follow-tags

.PHONY: release-major
release-major: test
	poetry run bump2version major
	git push --follow-tags
