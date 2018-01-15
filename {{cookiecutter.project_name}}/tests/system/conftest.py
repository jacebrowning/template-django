# pylint: disable=redefined-outer-name,unused-argument

import os
import logging

import pytest
from splinter import Browser

from . import user


PORT = int(os.getenv('TEST_PORT', 8001))
SITE = os.getenv('TEST_SITE', f"http://localhost:{PORT}")
HEADLESS = bool(os.getenv('TEST_HEADLESS'))


def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('selenium').setLevel(logging.WARNING)


@pytest.yield_fixture(scope='session', autouse=True)
def browser():
    with Browser('firefox', headless=HEADLESS) as browser:
        user.browser = browser
        user.site = SITE
        user.visit("/")
        yield browser
