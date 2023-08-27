VIRTUAL_ENV ?= .venv

INPUT := {{cookiecutter.project_name}}
OUTPUT := demo_project

# MAIN ########################################################################

.PHONY: all
all: build
	make all -C $(OUTPUT) CI=true

.PHONY: dev
dev: install
	rm -rf $(OUTPUT)/*
	@ sleep 2 && touch $(INPUT)/pyproject.toml &
	poetry run watchmedo shell-command --command="make .all-verbose" --recursive --wait $(INPUT)

.PHONY: .all-verbose
.all-verbose:
	@ echo
	@ echo "Genereating and testing the demo project..."
	@ echo
	@ make all
	@ echo
	@ echo "All tests passed."

# DEPENDENCIES ################################################################

.PHONY: bootstrap
bootstrap:
	asdf plugin add python || asdf plugin update python
	asdf plugin add poetry https://github.com/asdf-community/asdf-poetry.git || asdf plugin update poetry
	asdf install

.PHONY: doctor
doctor:
	{{cookiecutter.project_name}}/bin/verchew

.PHONY: install
install: $(VIRTUAL_ENV)/.flag
 $(VIRTUAL_ENV)/.flag: poetry.lock
	@ poetry config virtualenvs.in-project true
	poetry install
	@ touch $@

ifndef CI
poetry.lock: pyproject.toml
	poetry lock --no-update
	@ touch $@
endif

# BUILD #######################################################################

.PHONY: build
build: install
	poetry run cookiecutter . --no-input --overwrite-if-exists
	unset CI && cd demo_project && make install

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf $(OUTPUT)
	rm -rf $(VIRTUAL_ENV)

.DEFAULT_GOAL := install
