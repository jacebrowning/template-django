# pylint: disable=redefined-outer-name,unused-argument

import os
import time
from contextlib import suppress

import log
import pytest
from splinter import Browser
from selenium.common.exceptions import WebDriverException

from . import user


PORT = int(os.getenv('TEST_PORT', '8001'))
SITE = os.getenv('TEST_SITE', f"http://localhost:{PORT}")
HEADLESS = bool(os.getenv('TEST_HEADLESS'))


def pytest_configure(config):
    log.init()
    log.silence('selenium', allow_warning=True)


@pytest.fixture(scope='session', autouse=True)
def browser():
    with Browser('firefox', headless=HEADLESS) as browser:
        user.browser = browser
        user.site = SITE

        start = time.time()
        while site_loading():
            time.sleep(1)
            if time.time() - start > 60:
                raise RuntimeError("Site failed to load")
        time.sleep(1)

        yield browser


def site_loading():
    with suppress(WebDriverException):
        user.visit("/")

    loaded = user.browser.is_text_present("{{cookiecutter.project_name}}")

    return not loaded
