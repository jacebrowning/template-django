VIRTUAL_ENV ?= .venv

INPUT := {{cookiecutter.project_name}}
OUTPUT := demo_project

# MAIN ########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build
	make ci -C $(OUTPUT)

.PHONY: watch
watch: install
	rm -rf $(OUTPUT)/*
	@ sleep 2 && touch $(INPUT)/poetry.lock &
	poetry run watchmedo shell-command --command="clear; make ci" --recursive --wait $(INPUT)

# DEPENDENCIES ################################################################

.PHONY: install
install: $(VIRTUAL_ENV)/.flag
 $(VIRTUAL_ENV)/.flag: poetry.lock
	@ poetry config virtualenvs.in-project true
	poetry install
	@ touch $@

ifndef CI
poetry.lock: pyproject.toml
	poetry lock
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
