export PIPENV_VENV_IN_PROJECT=true

ENV := .venv

DEMO := demo_project

# MAIN ########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build $(DEMO)/Pipfile.lock
	make ci -C $(DEMO)

.PHONY: watch
watch: install
	rm -rf $(DEMO)
	pipenv run watchmedo shell-command --command="clear; make ci" --recursive --wait {{cookiecutter.project_name}}

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
	rm -rf $(DEMO)
	rm -rf $(ENV)
