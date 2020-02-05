import pytest
import requests

def pytest_addoption(parser):
    """Добавляем два параметра"""
    parser.addoption("--status_code", action="store", default="200", help="This is status code")
    parser.addoption("--url", action="store", default="ya.ru", help="This is url")


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
    assert response.status_code == get_param["status_code"]
