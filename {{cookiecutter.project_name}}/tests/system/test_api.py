# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from expecter import expect


from . import user


def describe_docs():

    def as_public_user():
        user.logout()
        user.visit("/api/docs")

        expect(user.browser.title) == "Swagger UI"
        expect(user.browser).has_text("{{cookiecutter.project_name}} API")
