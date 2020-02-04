import pytest
import requests
import json
from jsonschema import validate


def test_list_by_city(by_city_param):
    """Проверяем запрос по городу, с параметризацией фикстурой"""
    url = "https://api.openbrewerydb.org/breweries?by_city={!s}".format(by_city_param)
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("city", ["san_diego", "new_york"])
@pytest.mark.parametrize("brewery_type", ["large", "brewpub"])
def test_by_state_and_type(city, brewery_type):
    url = "https://api.openbrewerydb.org/breweries?by_city={!s}&by_type={!s}".format(city, brewery_type)
    response = requests.get(url).json()
    assert len(response) > 0


def test_search_by_name():
    url = "https://api.openbrewerydb.org/breweries?by_name=dog"
    response = requests.get(url).json()
    for i in response:
        assert i["name"].lower().find("dog") != -1


