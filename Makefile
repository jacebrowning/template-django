export PIPENV_VENV_IN_PROJECT=true

ENV := .venv

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
	@ sleep 2 && touch $(INPUT)/Pipfile &
	pipenv run watchmedo shell-command --command="clear; make ci" --recursive --wait $(INPUT)

# DEPENDENCIES ################################################################

.PHONY: install
install: $(ENV)
$(ENV): Pipfile*
	pipenv install
	@ touch $@

# BUILD #######################################################################

.PHONY: build
build: install
	pipenv run cookiecutter . --no-input --overwrite-if-exists
	cd demo_project && pipenv install --dev

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf $(OUTPUT)
	rm -rf $(ENV)
