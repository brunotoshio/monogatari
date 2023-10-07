
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
	poetry version patch
	it add pyproject.toml src/monogatari/__init__.py
	git commit -m "Bump version to $(shell poetry version -s)"
	git tag -a "release-$(shell poetry version -s)" -m "Version $(shell poetry version -s)"
	git push --follow-tags

.PHONY: release-minor
release-minor: test
	poetry version minor
	it add pyproject.toml src/monogatari/__init__.py
	git commit -m "Bump version to $(shell poetry version -s)"
	git tag -a "release-$(shell poetry version -s)" -m "Version $(shell poetry version -s)"
	git push --follow-tags

.PHONY: release-major
release-major: test
	poetry version major
	it add pyproject.toml src/monogatari/__init__.py
	git commit -m "Bump version to $(shell poetry version -s)"
	git tag -a "release-$(shell poetry version -s)" -m "Version $(shell poetry version -s)"
	git push --follow-tags
