REST API для управления каталогом товаров

Описание проекта
Этот проект реализует REST API для управления каталогом товаров магазина. Данные хранятся в файле `items.json`. API поддерживает операции CRUD и защищен HTTP Basic аутентификацией.

---

Установка и запуск

1. Убедитесь, что Python установлен:

   python3 --version

2.	Установите зависимости:

pip install flask flask-httpauth


3.	Запустите сервер:

python3 app.py


Сервер будет доступен по адресу http://127.0.0.1:8000.

Аутентификация

API защищено HTTP Basic аутентификацией:
	•	Логин: admin
	•	Пароль: password123

Эндпоинты и примеры запросов для Postman

1. Получить все товары
	•	Метод: GET
	•	URL: http://127.0.0.1:8000/items
	•	Заголовки:
	•	Authorization: Basic Auth (логин: admin, пароль: password123)

2. Добавить новый товар
	•	Метод: POST
	•	URL: http://127.0.0.1:8000/items
	•	Заголовки:
	•	Authorization: Basic Auth (логин: admin, пароль: password123)
	•	Content-Type: application/json
	•	Тело запроса:

{
    "id": 3,
    "name": "Tablet",
    "price": 300
}


3. Получить товар по ID
	•	Метод: GET
	•	URL: http://127.0.0.1:8000/items/1
	•	Заголовки:
	•	Authorization: Basic Auth (логин: admin, пароль: password123)


4. Обновить товар
	•	Метод: PUT
	•	URL: http://127.0.0.1:8000/items/1
	•	Заголовки:
	•	Authorization: Basic Auth (логин: admin, пароль: password123)
	•	Content-Type: application/json
	•	Тело запроса:

{
    "price": 950
}

5. Удалить товар
	•	Метод: DELETE
	•	URL: http://127.0.0.1:8000/items/1
	•	Заголовки:
	•	Authorization: Basic Auth (логин: admin, пароль: password123)

Структура файла items.json

Пример содержимого файла после выполнения запросов:

[
    {
        "id": 2,
        "name": "Phone",
        "price": 500
    },
    {
        "id": 3,
        "name": "Tablet",
        "price": 300
    }
]

Автор
Kateryna