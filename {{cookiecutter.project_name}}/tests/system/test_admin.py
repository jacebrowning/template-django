# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from . import user


def describe_login():

    def placeholder(expect):
        user.visit("/admin")

        expect(user.browser.title) == "Log in | demo_project Admin"
