"""Configuration file for sniffer."""

import os
import subprocess

from sniffer.api import select_runnable, file_validator, runnable


watch_paths = [
    "config",
    "{{cookiecutter.project_name}}",
    "tests",
]


@select_runnable('application_targets')
@file_validator
def application_code(path):
    return matches(path, 'py', 'ini', 'cfg') and 'tests' not in path


@select_runnable('unit_targets')
@file_validator
def unit_tests(path):
    return matches(path, 'py', 'ini', 'cfg') and 'unit' in path


@select_runnable('integration_targets')
@file_validator
def integration_tests(path):
    return matches(path, 'py', 'ini', 'cfg') and 'integration' in path


@select_runnable('system_targets')
@file_validator
def system_tests(path):
    return matches(path, 'py', 'ini', 'cfg') and 'system' in path


@runnable
def application_targets(*_):
    return call("make test-unit test-integration check")


@runnable
def unit_targets(*_):
    return call("make test-unit check")


@runnable
def integration_targets(*_):
    return call("make test-integration check")


@runnable
def system_targets(*_):
    return call("make test-system check")


def matches(path, *extensions):
    extension = path.split('.')[-1]
    return extension in extensions


def call(command):
    print('\n' + f"$ {command}")
    os.environ['DISABLE_COVERAGE'] = 'true'
    success = subprocess.call(command, shell=True) == 0
    return success
