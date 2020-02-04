import pytest

import pytest
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        help="This is request url"
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture(params=["san_diego", "new_york"])
def by_city_param(request):
    return request.param
