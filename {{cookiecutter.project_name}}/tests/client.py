# pylint: disable=broad-except

"""
Command-line client to manually interact with the running application.

Usage:

    pipenv run python tests/client.py <function> [<arguments>]

"""

import os
import time

import fire
from splinter import Browser

from .system import user


SITE = os.getenv('TEST_SITE', "http://localhost:8000")


def run():
    with Browser('firefox') as user.browser:
        _launch_browser()
        _execute_command()
        _wait_for_browser_close()


def _launch_browser():
    user.site = SITE
    user.visit("/")


def _execute_command():
    print("Running command...")
    try:
        fire.Fire(user)
    except Exception as exception:
        print(exception)
    print()


def _wait_for_browser_close():
    print("Close the browser window or ctrl+c to exit...")
    while True:
        try:
            if user.browser.url:
                time.sleep(0.1)
        except (Exception, KeyboardInterrupt):
            break
    print()


if __name__ == '__main__':
    run()
