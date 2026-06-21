import pytest
import allure
import helpers as H
from burgers_api_client import BurgersApiClient


@allure.feature("Пользователи")
@allure.story("Авторизация")
class TestUserLogin:

    @allure.title("Вход под существующим пользователем")
    @allure.description("Проверяет успешный вход с верными данными")
    def test_login_existing_user(self, registered_user):
        
        api = BurgersApiClient()
        payload = H.get_login_payload(
            email=registered_user["email"],
            password=registered_user["password"]
        )
        response = api.login_user(payload)
        
        assert response.status_code == 200

    @allure.title("Вход с неверным логином и паролем")
    @allure.description("Проверяет, что вход с некорректными данными возвращает 401")
    @pytest.mark.parametrize("email, password", [
        ("wrong@ya.com", "password123"),
        ("test@ya.com", "wrongpass"),
    ])
    def test_login_invalid_credentials_returns_error(self, email, password):
        
        api = BurgersApiClient()
        payload = H.get_login_payload(email=email, password=password)
        response = api.login_user(payload)
        
        assert response.status_code == 401