import pytest
import requests
from jsonschema import validate


schema_of_sub_breeds = {
    "type": "object",
    "properties": {
        "message": {"type": "array",
                    "items": {
                        "type": "string",
                        "examples": [
                            "afghan",
                            "basset",
                            "blood",
                            "english",
                            "ibizan",
                            "plott",
                            "walker"
                        ],
                        "pattern": "^(.*)$"
                    }
                    },
        "status": {
            "type": "string",
            "examples": [
                "success"
            ],
            "pattern": "^(.*)$"
        }
    }
}


def test_dogs_sub_breeds_schema():
    """Проверяем схему json списка под пород"""

    r = requests.get('https://dog.ceo/api/breed/hound/list')
    validate(instance=r.json(), schema=schema_of_sub_breeds)


@pytest.mark.parametrize("breed", ["boxer", "cairn", "borzoi"])
def test_single_random_img(breed):
    """Параметризация одним парамтером"""
    url = 'https://dog.ceo/api/breed/{!s}/images/random'.format(breed)
    response = requests.get(url)
    response_dict = response.json()
    assert response_dict["status"] == "success"


def test_list_all_breeds():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    print(r.headers.items())
    assert r.headers['Content-Type'] == 'application/json'


def test_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    response_dict = response.json()
    assert response_dict["status"] == "success"
