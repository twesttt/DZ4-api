import pytest
import requests


def test_list_by_city(by_city_param):
    """Проверяем запрос по городу, с параметризацией фикстурой"""

    url = "https://api.openbrewerydb.org/breweries?by_city={!s}".format(by_city_param)
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("city", ["san_diego", "new_york"])
@pytest.mark.parametrize("brewery_type", ["large", "brewpub"])
def test_by_state_and_type(city, brewery_type):
    """Проверяем запрос по двум фильтрам: по городу и по типу пивной"""

    url = "https://api.openbrewerydb.org/breweries?by_city={!s}&by_type={!s}".format(city, brewery_type)
    response = requests.get(url).json()
    assert len(response) > 0


def test_search_by_name():
    """Проверяем поиск пивной по ключевому слову в наименовании пивной"""

    url = "https://api.openbrewerydb.org/breweries?by_name=dog"
    response = requests.get(url).json()
    for i in response:
        assert i["name"].lower().find("dog") != -1


def test_per_page_return():
    """Проверяем запрос на определенное количество пивных"""

    url = "https://api.openbrewerydb.org/breweries?per_page=30"
    response = requests.get(url).json()
    assert len(response) == 30


def test_get_brewery():
    """Проверяем запрос пивной по ID"""

    url = "https://api.openbrewerydb.org/breweries/5494"
    response = requests.get(url).json()
    assert response["name"] == "MadTree Brewing"

