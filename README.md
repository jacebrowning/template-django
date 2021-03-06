# Jace's Django Template

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for a typical Django application following modern packaging conventions. It utilizes popular libraries alongside Make and pipenv to fully automate all development and deployment tasks. Check out the live demo: [jacebrowning/template-django-demo](https://github.com/jacebrowning/template-django-demo)

[![Build Status](https://img.shields.io/travis/com/jacebrowning/template-django.svg)](https://travis-ci.com/jacebrowning/template-django)
## Features

* Settings broken out into local, staging, and production
* API using [Django REST Framework](http://www.django-rest-framework.org/)
* Unit and integration testing using `pytest`, `pytest-describe`, and `pytest-expecter`
* End-to-end testing using [Splinter](https://splinter.readthedocs.io/)
* `Makefile` for automating common development tasks:
    - Installing dependencies into a virtual environment using `pipenv`
    - Generate superuser and other fixtures to seed the database
    - Running tests against the backend and frontend
    - Running style checkers (`pycodestyle`/`pydocstyle`) and linters (`pylint`)
* Continuous Integration via [CircleCI](https://circleci.com/docs/2.0/)
* Continuous Delivery via [Heroku](https://www.heroku.com/flow)

If you are instead looking for a [Python library](https://caremad.io/posts/2013/07/setup-vs-requirement/) template, check out [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

## Usage

Install `cookiecutter` and generate a project:

```
$ pip install cookiecutter
$ cookiecutter gh:jacebrowning/template-django -f
```

Cookiecutter will ask you for some basic info (your name, project name, first app name, etc.) and generate a base Django project for you. Once created, run the code formatter to updates files based on your chosen names:

```
$ cd <github_repo>
$ make format
```

## Updates

Checkout the appropriate branch of [template-django-demo](https://github.com/jacebrowning/template-django-demo) and manually merge changes into your project.

