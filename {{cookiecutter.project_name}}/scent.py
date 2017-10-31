"""Configuration file for sniffer."""

import time
import subprocess

from sniffer.api import select_runnable, file_validator, runnable
try:
    from pync import Notifier
except ImportError:
    notify = None
else:
    notify = Notifier.notify


watch_paths = [
    "backend",
    "config",
    "frontend",
    "tests",
]

class options:
    group = int(time.time())
    rerun_args = None
    initial_run = True

    @classmethod
    def skip(cls):
        should_skip = cls.initial_run
        cls.initial_run = False
        return should_skip


@select_runnable('backend_targets')
@file_validator
def backend_files(path):
    return matches(path, 'py', 'ini') and 'system' not in path


@select_runnable('frontend_targets')
@file_validator
def frontend_files(path):
    return matches(path, 'clj', 'cljs')


@select_runnable('system_targets')
@file_validator
def system_files(path):
    return matches(path, 'py', 'ini') and 'system' in path


def matches(path, *extensions):
    extension = path.split('.')[-1]
    return extension in extensions


@runnable
def backend_targets(*_args):
    return run("Backend", [
        ("Unit Tests", "make test-backend-unit DISABLE_COVERAGE=true", True),
        ("Integration Tests", "make test-backend-all", False),
        ("Static Analysis", "make check-backend", True),
    ])


@runnable
def frontend_targets(*_args):
    return run("Frontend", [
        ("Unit Tests", "make test-frontend-unit", True),
        ("Static Analysis", "make check-frontend", True),
    ])


@runnable
def system_targets(*_args):
    if options.skip():
        return True
    return run("System", [
        ("Tests", "make test-system", False),
        ("Static Analysis", "make check-backend", True),
    ])

def run(name, targets):
    count = 0
    for count, (title, command, retry) in enumerate(targets, start=1):

        success = call(f"{name} {title}", command, retry)
        if not success:
            message = "✅ " * (count - 1) + "❌"
            show_notification(message, f"{name} {title}")

            return False

    message = "✅ " * count
    title = f"All {name} Targets"
    show_notification(message, title)

    return True


def call(title, command, retry):
    if options.rerun_args:
        title, command, retry = options.rerun_args
        options.rerun_args = None
        success = call(title, command, retry)
        if not success:
            return False

    print(f"\n\n$ {command}")
    failure = subprocess.call(command, shell=True)

    if failure and retry:
        options.rerun_args = title, command, retry

    return not failure


def show_notification(message, title):
    if notify and title:
        notify(message, title=title, group=options.group)
