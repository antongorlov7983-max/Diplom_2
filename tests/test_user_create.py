import pytest
import allure
import helpers as H
from burgers_api_client import BurgersApiClient


@allure.feature("Пользователи")
@allure.story("Создание пользователя")
class TestUserCreate:

    @allure.title("Создать уникального пользователя")
    @allure.description("Проверяет, что пользователь успешно создаётся с валидными данными")
    def test_create_unique_user(self, user_cleanup):
        
        api = BurgersApiClient()
        payload = H.get_register_payload()
        response = api.register_user(payload)
        
        assert response.status_code == 200
        data = response.json()
        user_cleanup(data["accessToken"])
        assert data["user"]["email"] == payload["email"]
        assert data["accessToken"] is not None


    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_duplicate_user_returns_error(self, registered_user, user_cleanup):
        
        api = BurgersApiClient()
        payload = H.get_register_payload(
            email=registered_user["email"],
            password=registered_user["password"],
            name=registered_user["name"]
        )
        response = api.register_user(payload)
       
        if response.status_code == 200:
            token = response.json().get("accessToken")
            user_cleanup(token)
        assert response.status_code == 403

    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    @allure.title("Создать пользователя без поля {missing_field}")
    def test_create_user_missing_field_returns_error(self, missing_field, user_cleanup):
        
        api = BurgersApiClient()
        payload = H.get_payload_without_field(missing_field)
        response = api.register_user(payload)
        
        if response.status_code == 200:
            token = response.json().get("accessToken")
            user_cleanup(token)
        assert response.status_code == 403