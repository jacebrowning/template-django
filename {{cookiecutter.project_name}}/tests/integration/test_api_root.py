# pylint: disable=unused-variable,unused-argument,expression-not-assigned,redefined-outer-name

import pytest


def describe_root():

    @pytest.fixture
    def index():
        return "/api/"

    def describe_GET():

        def it_always_returns_200(expect, client, index):
            response = client.get(index)

            expect(response.status_code) == 200
