import pytest


@pytest.fixture(params=["san_diego", "new_york"])
def by_city_param(request):
    return request.param


@pytest.fixture(params=["comments", "albums", "posts"])
def nested_resources(request):
    return request.param
