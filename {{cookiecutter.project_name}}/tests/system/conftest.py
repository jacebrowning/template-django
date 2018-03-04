# pylint: disable=redefined-outer-name,unused-argument

import os

import pytest
from splinter import Browser
import log

from . import user


PORT = int(os.getenv('TEST_PORT', 8001))
SITE = os.getenv('TEST_SITE', f"http://localhost:{PORT}")
HEADLESS = bool(os.getenv('TEST_HEADLESS'))


def pytest_configure(config):
    log.init(debug=True)
    log.silence('selenium', allow_warning=True)


@pytest.yield_fixture(scope='session', autouse=True)
def browser():
    with Browser('firefox', headless=HEADLESS) as browser:
        user.browser = browser
        user.site = SITE
        user.visit("/")
        yield browser
