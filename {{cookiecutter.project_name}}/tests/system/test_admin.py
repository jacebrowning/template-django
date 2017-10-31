# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from expecter import expect


from . import user


def describe_login():

    def with_valid_credentials():
        user.login('admin', 'password')

        user.visit("/admin")

        expect(user.browser).has_text("{{cookiecutter.project_name}} Administration")
        expect(user.browser).has_text("Select a model")

    def with_invalid_credentials():
        user.login('bad-username', 'bad-password')

        user.visit("/admin")

        expect(user.browser.title) == "Log in | {{cookiecutter.project_name}}"
        expect(user.browser).has_text("{{cookiecutter.project_name}} Administration")
