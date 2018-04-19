REPOSITORY := {{cookiecutter.github_username}}/{{cookiecutter.github_repo}}

ifdef CIRCLECI
	RUN := pipenv run
else ifdef HEROKU_APP_NAME
	SKIP_INSTALL := true
else
	RUN := pipenv run
endif

.PHONY: all
all: install

.PHONY: ci
ci: check test ## CI | Run all validation targets

.PHONY: watch
watch: install ## CI | Rerun all validation targests in a loop
	@ rm -rf $(FAILURES)
	$(RUN) sniffer

# SYSTEM DEPENDENCIES #########################################################

.PHONY: doctor
doctor: ## Check for required system dependencies
	bin/verchew

.envrc:
	echo export SECRET_KEY=local >> $@
	echo export DATABASE_URL=postgresql://localhost/{{cookiecutter.project_name}}_dev >> $@
	echo export REDIS_URL=redis://127.0.0.1:6379/0 >> $@
	echo >> $@
	echo export TEST_EMAILS=you@yourdomain.com >> $@
	- direnv allow

# PROJECT DEPENDENCIES ########################################################

export PIPENV_VENV_IN_PROJECT=true
VENV := .venv

BACKEND_DEPENDENCIES := $(VENV)/.pipenv-$(shell bin/checksum Pipfile*)
FRONTEND_DEPENDENCIES :=

.PHONY: install
ifndef SKIP_INSTALL
install: $(BACKEND_DEPENDENCIES) $(FRONTEND_DEPENDENCIES) ## Install project dependencies
endif

$(BACKEND_DEPENDENCIES):
	pipenv install --dev
	@ touch $@

$(FRONTEND_DEPENDENCIES):
	# TODO: Install frontend dependencies if applicable
	@ touch $@

.PHONY: clean
clean:
	rm -rf staticfiles
	rm -rf .coverage htmlcov

.PHONY: clean-all
clean-all: clean
	# TODO: Delete all frontend files
	rm -rf $(VENV)

# RUNTIME DEPENDENCIES ########################################################

.PHONY: migrations
migrations: install  ## Database | Generate database migrations
	$(RUN) python manage.py makemigrations

.PHONY: migrate
migrate: install ## Database | Run database migrations
	$(RUN) python manage.py migrate

.PHONY: data
data: install migrate ## Database | Seed data for manual testing
	$(RUN) python manage.py gendata $(TEST_EMAILS)
	# TODO: Load test data and fixtures
	# $(RUN) python manage.py loaddata content

.PHONY: reset
reset: install ## Database | Create a new database, migrate, and seed it
	- dropdb {{cookiecutter.project_name}}_dev
	- createdb {{cookiecutter.project_name}}_dev
	make data

# VALIDATION TARGETS ##########################################################

PYTHON_PACKAGES := config {{cookiecutter.project_name}}
FAILURES := .cache/v/cache/lastfailed

.PHONY: check
check: check-backend ## Run static analysis

.PHONY: check-backend
check-backend: install
	$(RUN) pylint $(PYTHON_PACKAGES) tests --rcfile=.pylint.ini
	$(RUN) pycodestyle $(PYTHON_PACKAGES) tests --config=.pycodestyle.ini

.PHONY: check-frontend
check-frontend: install
	# TODO: Run frontend linters if applicable

.PHONY: test
test: test-backend test-frontend ## Run all tests

.PHONY: test-backend
test-backend: test-backend-all

.PHONY: test-backend-unit
test-backend-unit: install
	@ ( mv $(FAILURES) $(FAILURES).bak || true ) > /dev/null 2>&1
	$(RUN) pytest $(PYTHON_PACKAGES) tests/unit
	@ ( mv $(FAILURES).bak $(FAILURES) || true ) > /dev/null 2>&1
	$(RUN) coverage.space $(REPOSITORY) unit

.PHONY: test-backend-integration
test-backend-integration: install
	@ if test -e $(FAILURES); then $(RUN) pytest --last-failed tests/integration; fi
	@ rm -rf $(FAILURES)
	$(RUN) pytest tests/integration
	$(RUN) coverage.space $(REPOSITORY) integration

.PHONY: test-backend-all
test-backend-all: install
	@ if test -e $(FAILURES); then $(RUN) pytest --last-failed $(PYTHON_PACKAGES) tests/integration; fi
	@ rm -rf $(FAILURES)
	$(RUN) pytest $(PYTHON_PACKAGES) tests/integration
	$(RUN) coverage.space $(REPOSITORY) overall

.PHONY: test-frontend
test-frontend: test-frontend-unit

.PHONY: test-frontend-unit
test-frontend-unit: install
	# TODO: Run frontend tests if applicable

.PHONY: test-system
test-system: install
	$(RUN) honcho start --procfile=tests/system/Procfile --env=tests/system/.env

# SERVER TARGETS ##############################################################

.PHONY: run
run: .envrc install ## Run the applicaiton
	$(RUN) honcho start --procfile=Procfile.dev --port=$${PORT:-8000}

.PHONY: run-production
run-production: .envrc install
	pipenv shell "bin/pre_compile; exit \$$?"
	pipenv shell "bin/post_compile; exit \$$?"
	pipenv shell "heroku local release; exit \$$?"
	pipenv shell "heroku local web; exit \$$?"

# RELEASE TARGETS #############################################################

.PHONY: build
build: install
	# TODO: Build frontend code for production if applicable

.PHONY: promote
promote: install
	TEST_SITE=https://staging.{{cookiecutter.project_name}}.com $(RUN) pytest tests/system --cache-clear
	heroku pipelines:promote --app {{cookiecutter.project_name}}-staging --to {{cookiecutter.project_name}}
	TEST_SITE=https://{{cookiecutter.project_name}}.com $(RUN) pytest tests/system

# HELP ########################################################################

.PHONY: help
help: all
	@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
