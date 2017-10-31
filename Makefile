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

$(DEMO)/Pipfile.lock: $(DEMO)/Pipfile
	cd $(DEMO) && pipenv install --dev --skip-lock && pipenv lock
	@ touch $@

# CLEANUP #####################################################################

.PHONY: clean
clean:
	rm -rf $(DEMO)
	rm -rf $(ENV)
