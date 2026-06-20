import requests
import allure
import data_test as DT


class BurgersApiClient:

    @allure.step("Регистрация пользователя")
    def register_user(self, payload):
        allure.attach(str(payload), "Тело запроса", allure.attachment_type.JSON)
        response = requests.post( f"{DT.BASE_URL}{DT.REGISTER_ENDPOINT}", json=payload)
        allure.attach(response.text, "Ответ сервера", allure.attachment_type.JSON)
        return response

    @allure.step("Логин пользователя")
    def login_user(self, payload):
        allure.attach(str({"email": payload["email"]}), "Логин", allure.attachment_type.JSON)
        response = requests.post(f"{DT.BASE_URL}{DT.LOGIN_ENDPOINT}", json=payload)
        allure.attach(response.text, "Ответ сервера", allure.attachment_type.JSON)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        response = requests.delete(f"{DT.BASE_URL}{DT.DELETE_USER_ENDPOINT}", headers={"Authorization": token})
        allure.attach(str(response.status_code), "Статус удаления", allure.attachment_type.TEXT)
        return response

    @allure.step("Получение списка ингредиентов")
    def get_ingredients(self):
        response = requests.get(f"{DT.BASE_URL}{DT.INGREDIENTS_ENDPOINT}")
        ingredients = response.json().get("data", [])
        hashes = [ing["_id"] for ing in ingredients[:2]]
        allure.attach(str(hashes), "Хеши ингредиентов", allure.attachment_type.TEXT)
        return response

    @allure.step("Создание заказа")
    def create_order(self, ingredients, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        allure.attach(str(ingredients), "Ингредиенты", allure.attachment_type.TEXT)
        response = requests.post(f"{DT.BASE_URL}{DT.ORDERS_ENDPOINT}", json={"ingredients": ingredients}, headers=headers)
        allure.attach(response.text, "Ответ сервера", allure.attachment_type.JSON)
        return response