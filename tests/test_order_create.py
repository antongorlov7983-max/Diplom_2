import allure
from burgers_api_client import BurgersApiClient


@allure.feature("Заказы")
@allure.story("Создание заказа")
class TestOrderCreate:

    @allure.title("Создать заказ с авторизацией и ингредиентами")
    @allure.description("Проверяет успешное создание заказа авторизованным пользователем")
    def test_create_order_with_auth_and_ingredients(self, registered_user, ingredient_hashes):
        
        api = BurgersApiClient()
        response = api.create_order(ingredient_hashes, registered_user["accessToken"])
        
        assert response.status_code == 200
        data = response.json()
        assert data.get("success") is True
        assert data["order"]["number"] is not None

    @allure.title("Создать заказ без авторизации")
    @allure.description("Проверяет, что заказ создаётся без токена (баг: документация требует авторизацию)")
    def test_create_order_without_auth_returns_error(self, ingredient_hashes):
        
        api = BurgersApiClient()
        response = api.create_order(ingredient_hashes)
        
        assert response.status_code == 401
        assert response.json().get("success") is True

    @allure.title("Создать заказ без ингредиентов")
    @allure.description("Проверяет, что создание заказа с пустым списком возвращает 400")
    def test_create_order_without_ingredients_returns_error(self, registered_user):
        
        api = BurgersApiClient()
        response = api.create_order([], registered_user["accessToken"])
        
        assert response.status_code == 400

    @allure.title("Создать заказ с неверным хешем ингредиентов")
    @allure.description("Проверяет, что создание заказа с невалидным хешем возвращает 500")
    def test_create_order_invalid_hash_returns_error(self, registered_user):
        
        api = BurgersApiClient()
        response = api.create_order(["invalid_hash_12345"], registered_user["accessToken"])
        
        assert response.status_code == 500