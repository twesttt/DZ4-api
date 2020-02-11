import pytest
import requests


def test_list_all_resources():
    """Проверяем запрос на список всех ресурсов"""

    url = "http://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert len(response.json()) == 100


def test_update_resource():
    """Проверяем возможность обновить информацию"""

    new_data = {
        "id": "1",
        "title": "hello",
        "body": "bar",
        "userId": "1"
    }

    url = "http://jsonplaceholder.typicode.com/posts/1"
    response = requests.put(url, json=new_data)
    response_dict = response.json()
    assert response_dict["title"] == "hello"


def test_create_resource():
    """Проверяем возможность создать новый пост"""

    new_data = {
        "title": "New post",
        "body": "bar",
        "userId": "1"
    }

    url = "http://jsonplaceholder.typicode.com/posts/"
    response = requests.post(url, json=new_data)
    print(response.text)
    response_dict = response.json()
    assert response_dict["id"] == 101


def test_nested_resources(nested_resources):
    """Проверяем получение вложенного ресурса"""

    url = "http://jsonplaceholder.typicode.com/posts/1/{!s}".format(nested_resources)
    response = requests.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize("post", ["1", "2"])
def test_delete_resources(post):
    """Проверяем возможность удаления ресурса"""

    url = "http://jsonplaceholder.typicode.com/posts/{!s}".format(post)
    response = requests.delete(url)
    assert response.status_code == 200
