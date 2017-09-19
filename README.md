# template-django

Generates the structure for a Django application using [cookiecutter][cookiecutter].

Unix: [![Unix Build Status](https://img.shields.io/travis/jacebrowning/template-django/master.svg)](https://travis-ci.org/jacebrowning/template-django)
Windows: [![Windows Build Status](https://img.shields.io/appveyor/ci/jacebrowning/template-django.svg)](https://ci.appveyor.com/project/jacebrowning/template-django)

This is a template for a typical Django application following modern packaging conventions. It utilizes popular libraries alongside Make and pipenv to fully automate all development and deployment tasks. Check out the live demo: [jacebrowning/template-django-demo](https://github.com/jacebrowning/template-django-demo)

If you are instead looking for a [Python library](https://caremad.io/posts/2013/07/setup-vs-requirement/) template, check out [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

## Get Started

Install `cookiecutter` and generate a project:

    $ pip install cookiecutter
    $ cookiecutter gh:jacebrowning/template-django -f

Cookiecutter will ask you for some basic info (your name, project name, python package name, etc.) and generate a base Python project for you.

## Features

* Preconfigured setup for [Travis-CI][travis], [Coveralls][coveralls], and [Scrutinizer][scrutinizer]
* `Makefile` for automating common development tasks:
    - Installing dependencies into a virtual environment using `pipenv`
    - Running tests
    - Running style checkers (`pycodestyle`/`pydocstyle`) and linters (`pylint`)

[cookiecutter]: https://github.com/audreyr/cookiecutter
[travis]: https://travis-ci.org/
[coveralls]: https://coveralls.io/
[scrutinizer]: https://scrutinizer-ci.com/
