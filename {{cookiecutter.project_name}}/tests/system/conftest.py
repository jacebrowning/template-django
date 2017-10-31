# pylint: disable=redefined-outer-name,unused-argument

import os
import time
import logging
from contextlib import suppress

import pytest
from splinter import Browser
from selenium.common.exceptions import WebDriverException

from . import user


def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('selenium').setLevel(logging.WARNING)


@pytest.yield_fixture(scope='session', autouse=True)
def browser():
    with Browser('firefox') as browser:
        user.site = os.getenv('SITE', "http://localhost:5001")
        user.browser = browser

        start = time.time()
        while site_loading():
            time.sleep(0.5)
            if time.time() - start > 10:
                raise RuntimeError("Site failed to load")

        yield


def site_loading():
    with suppress(WebDriverException):
        user.visit("/")

    loaded = user.browser.is_text_present("{{cookiecutter.project_name}}")

    return not loaded
