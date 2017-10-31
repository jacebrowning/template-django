export PIPENV_VENV_IN_PROJECT=true

ENV := .venv

# MAIN ########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build demo_project/Pipfile.lock
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

demo_project/Pipfile.lock:
	cd demo_project && pipenv lock

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf demo_project
	rm -rf $(ENV)
