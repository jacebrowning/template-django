# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from expecter import expect


from . import user


def describe_login():

    def placeholder():
        user.visit("/admin")

        expect(user.browser.title) == "Log in | demo_project Admin"
