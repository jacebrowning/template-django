# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from expecter import expect


from . import user


def describe_docs():

    def placeholder():
        user.visit("/api/docs")

        expect(user.browser.title) == "Swagger UI"
