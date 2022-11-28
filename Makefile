.PHONY: help clean

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@echo "clean | Remove all build, test, coverage and Python artifacts"
	@echo "clean-build | Remove build artifacts"
	@echo "clean-pyc | Remove Python file artifacts"
	@echo "clean-test | Remove test and coverage artifacts"
	@echo "run | Run the project in Docker"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf **/*.egg-info
	rm -rf static/CACHE

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -rf .pytest_cache; \
	rm -rf .ipython/profile_default; \
	rm -rf htmlcov; \
	rm -rf build; \
	rm -f .coverage; \
	rm -f coverage.xml; \
	rm -f junit.xml; \
	rm -rf .hypothesis; \
	find . -name '*.py,cover' -exec rm -f {} +

fix-file-permissions:
	sudo chown $$USER:$$USER src/fobi/migrations/ -R || true
	sudo chown $$USER:$$USER src/fobi/contrib/apps/djangocms_integration/migrations/ -R || true
	sudo chown $$USER:$$USER src/fobi/contrib/apps/wagtail_integration/migrations/ -R || true
	sudo chown $$USER:$$USER src/fobi/contrib/form_handlers/db_store/migrations/ -R || true
	sudo chown $$USER:$$USER examples/simple/page/migrations/ -R || true
	sudo chown $$USER:$$USER tmp/ -R || true

run: prepare-required-files
	docker-compose -f docker-compose.yml up --remove-orphans;

build: prepare-required-files
	docker-compose -f docker-compose.yml build;

build-%: prepare-required-files
	docker-compose -f docker-compose.yml build $*;

stop:
	docker-compose -f docker-compose.yml stop;

touch:
	docker-compose -f docker-compose.yml exec backend touch manage.py

make-migrations:
	docker-compose -f docker-compose.yml exec backend ./manage.py makemigrations $(APP);

migrate:
	docker-compose -f docker-compose.yml exec backend ./manage.py migrate $(APP);

test:
	docker-compose -f docker-compose.yml exec backend pytest /backend/src/$(TEST_PATH);

tox-test:
	docker-compose -f docker-compose.yml exec backend tox -e $(ARGS);

tox-list:
	docker-compose -f docker-compose.yml exec backend tox -l;

show-migrations:
	docker-compose -f docker-compose.yml exec backend ./manage.py showmigrations

show-urls:
	docker-compose -f docker-compose.yml exec backend ./manage.py show_urls

shell:
	docker-compose -f docker-compose.yml exec backend python examples/simple/manage.py shell

create-superuser:
	docker-compose -f docker-compose.yml exec backend python examples/simple/manage.py createsuperuser

fobi-sync-plugins:
	docker-compose -f docker-compose.yml exec backend ./manage.py fobi_sync_plugins

pip-install:
	docker-compose -f docker-compose.yml exec backend pip install -r requirements/local.txt

pip-list:
	docker-compose -f docker-compose.yml exec backend pip list

pip-compile:
	docker-compose -f docker-compose.yml exec backend pip install --upgrade pip && pip install pip-tools
	docker-compose -f docker-compose.yml exec backend ls -al /backend/examples/requirements/
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile captcha.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile common.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile debug.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile demo.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile deployment.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile dev.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile django_2_2.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile django_3_0.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile django_3_1.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile django_3_2.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile django_4_0.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile django_4_1.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile djangocms_3_4_3.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile djangorestframework.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile docs.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile feincms_1_17.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile feincms_1_20.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile latest.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile mptt.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile recaptcha.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile style_checkers.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile test.in
	docker-compose -f docker-compose.yml exec -w /backend/examples/requirements/ backend pip-compile testing.in

black:
	docker-compose -f docker-compose.yml exec backend black .

isort:
	docker-compose -f docker-compose.yml exec backend isort . --overwrite-in-place

bash:
	docker-compose -f docker-compose.yml run backend /bin/bash

prepare-required-files:
	mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
	mkdir -p examples/media/fobi_plugins/file

release:
	python setup.py register
	python setup.py sdist bdist_wheel
	twine upload dist/* --verbose
