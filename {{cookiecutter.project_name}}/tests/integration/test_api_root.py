# pylint: disable=unused-variable,unused-argument,expression-not-assigned,redefined-outer-name

import pytest
from expecter import expect


def describe_root():

    @pytest.fixture
    def index():
        return "/api/"

    def describe_GET():

        def it_always_returns_200(client, index):
            response = client.get(index)

            expect(response.status_code) == 200
