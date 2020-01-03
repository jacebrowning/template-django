# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from . import user


def describe_docs():

    def placeholder(expect):
        user.visit("/api/docs")

        expect(user.browser.html).contains("Swagger")
