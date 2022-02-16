VIRTUAL_ENV ?= .venv

INPUT := {{cookiecutter.project_name}}
OUTPUT := demo_project

# MAIN ########################################################################

.PHONY: all
all: install

.PHONY: ci
ci: build
	make ci -C $(OUTPUT) CI=true

.PHONY: dev
dev: install
	rm -rf $(OUTPUT)/*
	@ sleep 2 && touch $(INPUT)/pyproject.toml &
	poetry run watchmedo shell-command --command="make .ci-verbose" --recursive --wait $(INPUT)

.PHONY: .ci-verbose
.ci-verbose:
	@ echo
	@ echo "Genereating and testing the demo project..."
	@ echo
	@ make ci
	@ echo
	@ echo "All tests passed."

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
