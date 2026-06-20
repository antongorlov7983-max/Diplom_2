import pytest
import allure
import helpers as H
from burgers_api_client import BurgersApiClient


@pytest.fixture
def user_cleanup():
    api = BurgersApiClient()
    tokens = []

    def add_for_cleanup(token):
        tokens.append(token)

    yield add_for_cleanup

    for token in tokens:
        api.delete_user(token)


@pytest.fixture
def registered_user(user_cleanup):
    api = BurgersApiClient()
    payload = H.get_register_payload()

    with allure.step("Создать уникального пользователя"):
        response = api.register_user(payload)
        assert response.status_code == 200
        data = response.json()

    user_cleanup(data["accessToken"])
    return {
        "email": data["user"]["email"],
        "name": data["user"]["name"],
        "password": payload["password"],
        "accessToken": data["accessToken"]
    }


@pytest.fixture
def ingredient_hashes():
    api = BurgersApiClient()
    response = api.get_ingredients()
    ingredients = response.json().get("data", [])
    return [ing["_id"] for ing in ingredients[:2]]