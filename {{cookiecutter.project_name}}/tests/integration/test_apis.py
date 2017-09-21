# pylint: disable=redefined-outer-name,unused-variable,unused-argument,expression-not-assigned

import pytest
from expecter import expect
from rest_framework.test import APIClient

from {{cookiecutter.first_app_name}}.models import Pattern, Search, Result


@pytest.fixture
def client():
    return APIClient()


def describe_memes():

    @pytest.fixture
    def url():
        return "/api/foo/"

    def describe_GET():

        def it_requires_text_and_source(client, url):
            response = client.get(url)

            expect(response.status_code) == 400
            expect(response.data) == {
                'text': ["This field is required."],
                'source': ["This field is required."],
            }

