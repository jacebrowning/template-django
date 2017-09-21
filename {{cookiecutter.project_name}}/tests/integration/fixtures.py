# pylint: disable=unused-argument,redefined-outer-name

import pytest

from {{cookiecutter.first_app_name}}.models import Pattern


@pytest.fixture
def pattern(db):
    return Pattern.objects.create(
        regex="(.+) all the (.+)",
        key="xy",
        top=r"\1",
        bottom=r"all the \2",
    )
