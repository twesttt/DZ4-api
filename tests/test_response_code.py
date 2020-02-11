import pytest
import requests


@pytest.fixture
def get_param(request):
    """Получаем значения параметров в словарь"""

    config_param = {}
    config_param["url"] = request.config.getoption("--url")
    config_param["status_code"] = request.config.getoption("--status_code")
    return config_param


def test_response(get_param):
    """Отправляем get запрос по полученному url и сверяем статусы ответа"""

    response = requests.get(get_param["url"])
    assert response.status_code == int(get_param["status_code"])
