# For Contributors

## Setup

### Requirements

* Make:
    * Windows: http://mingw.org/download/installer
    * Mac: http://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make
* Python: `$ pyenv install`
* Poetry: https://python-poetry.org/docs/#installation

To confirm these system dependencies are configured correctly:

```sh
$ make doctor
```

### Installation

Install project dependencies into a virtual environment:

```sh
$ make install
```

## Development Tasks

### Testing

Manually run the tests:

```sh
$ make test
```

or keep them running on change:

```sh
$ make watch
```

> In order to have OS X notifications, `brew install terminal-notifier`.


### Static Analysis

Run linters and static analyzers:

```sh
$ make pylint
$ make pycodestyle
$ make pydocstyle
$ make check  # includes all checks
```

## Continuous Integration

The CI server will report overall build status:

```sh
$ make ci
```
