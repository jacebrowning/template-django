# pylint: disable=redefined-outer-name,unused-argument

import os
import logging

import pytest
from splinter import Browser

from . import user


def pytest_configure(config):
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('selenium').setLevel(logging.WARNING)


@pytest.yield_fixture(scope='session', autouse=True)
def browser():
    with Browser('firefox') as browser:
        user.browser = browser
        user.site = os.getenv('SITE', "http://localhost:8001")
        user.visit("/")
        yield browser
