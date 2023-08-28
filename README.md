# Jace's Django Template

This is a [cookiecutter](https://github.com/audreyr/cookiecutter) template for a typical Django project following modern packaging conventions. It utilizes popular libraries alongside Make and Poetry to fully automate all development and deployment tasks. Check out the live demo: [jacebrowning/template-django-demo](https://github.com/jacebrowning/template-django-demo)

[![Build Status](https://img.shields.io/travis/com/jacebrowning/template-django.svg)](https://app.travis-ci.com/github/jacebrowning/template-django)
## Features

* Settings broken out into local, staging, and production
* API using [Django REST Framework](http://www.django-rest-framework.org/)
* Unit and integration testing using `pytest`, `pytest-describe`, and `pytest-expecter`
* End-to-end testing using [Splinter](https://splinter.readthedocs.io/)
* `Makefile` for automating common development tasks:
    - Installing dependencies into a virtual environment using `poetry`
    - Generate superuser and other fixtures to seed the database
    - Running tests against the backend and frontend
    - Running type checks (`mypy`) and linters (`pylint`)
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

## Deploying

This template builds projects intended to be deployed on Heroku:

```
$ heroku buildpacks:clear
$ heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
$ heroku buildpacks:add heroku/python
```

You'll also need to set the following environment variables in all environments:

| Name | Value | Purpose |
| --- | --- | --- |
| `DISABLE_COLLECTSTATIC` | `true` | Disable automatic static files collection since `bin/post_compile` already does that |
| `HEROKU_APP_NAME` | `[staging-]<domain>` | Infer the domain name for staging and production |
| `DJANGO_SETTINGS_MODULE` | `config.settings.[staging]` | Specify which Django settings to use for the application |
| `SECRET_KEY` | `<generated>` | Securely encrypt passwords in the database |
| `DATABASE_URL` | `postgres://USER:PASSWORD@HOST:PORT/NAME` | Specify the database URL for the application to use, following the schema used by [dj_database_url](https://github.com/kennethreitz/dj-database-url#url-schema) |
| `BUGSNAG_API_KEY` | `<secret>` | Optional API key to enable the Bugsnag integration |
| `MAX_REQUESTS[_JITTER]` | `<int>` | Optional values to help deal with [memory leaks](https://docs.gunicorn.org/en/stable/settings.html?highlight=memory%20leaks#max-requests) |

## Updates

Run the update tool, which is generated inside each project:

```
$ bin/update
```
