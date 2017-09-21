# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

import pytest
from expecter import expect

from . import user


def describe_navbar():

    def describe_logo():

        def it_shows_stuff():
            user.goto_index()
            expect(user.browser.url) == user.site + "/"
            expect(user.browser.html).contains("Sample Results")
            expect(user.browser.html.count("/share/")) == 12
