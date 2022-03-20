# pylint: disable=redefined-outer-name,unused-variable,unused-argument,expression-not-assigned

import pytest

def describe_status():
    @pytest.fixture
    def url():
        return "/"

    def it_contains_the_date(expect, client, url):
        response = client.get(url)

        html = response.content.decode()
        expect(html).includes("2022")
