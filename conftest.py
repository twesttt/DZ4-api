import pytest


@pytest.fixture(params=["san_diego", "new_york"])
def by_city_param(request):
    return request.param


@pytest.fixture(params=["comments", "albums", "posts"])
def nested_resources(request):
    return request.param


def pytest_addoption(parser):
    """Добавляем два параметра"""

    parser.addoption("--status_code", action="store", default=200, help="This is status code")
    parser.addoption("--url", action="store", default="http://ya.ru", help="This is url")


