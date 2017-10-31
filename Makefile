export PIPENV_SHELL_COMPAT=true
export PIPENV_VENV_IN_PROJECT=true

ENV := .venv

# MAIN ########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build
	make ci -C demo_project

.PHONY: watch
watch: install
	pipenv run watchmedo shell-command --command="clear; make ci" --recursive {{cookiecutter.project_name}}

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

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf demo_project
	rm -rf $(ENV)
