# final_project_API_test / Stellar Burgers API Tests

Автотесты для учебного сервиса Stellar Burgers. Проверяют корректность работы ручек API: коды ответов, тела, обработку ошибок.

## Тестовые данные

- Пользователи создаются перед тестом и удаляются после
- Генерация случайных email, паролей, имён
- Параметризация для проверки разных сценариев

## Allure-отчёт

| Декоратор | Назначение |
|---|---|
| `@allure.feature` | Группировка по ручкам |
| `@allure.story` | Сценарии внутри ручек |
| `@allure.step` | Шаги запросов в отчёте |
| `@allure.attach` | Вложение тела запроса и ответа |
| `@allure.title` | Название теста |
| `@allure.description` | Описание теста |

## Запуск

pip install -r requirements.txt
pytest --alluredir=allure-results -v
allure serve allure-results

## Результаты

11 тестов пройдены
1 тест не прошел