

Тестирование и создание клиента для REST API

Описание проекта
В рамках задания выполнено:
1. Тестирование веб-сервиса через Postman.
2. Написание клиента для взаимодействия с веб-сервисом с использованием библиотеки `requests`.

---

Тестирование в Postman

Предварительные шаги:
   1. Убедитесь, что сервер запущен:
      python3 app.py

	2.	Убедитесь, что сервер доступен по адресу http://127.0.0.1:8000.

Запросы в Postman
	1.	GET /items: Получить весь каталог товаров:
	•	URL: http://127.0.0.1:8000/items
	•	Метод: GET
	•	Авторизация: Basic Auth (логин: admin, пароль: password123).


Пример использования
if __name__ == "__main__":
    # Получить все товары
    get_items()

    # Добавить новый товар
    add_item("Tablet", 300, "White")

    # Обновить товар с ID 1
    update_item(1, name="Updated Laptop", price=1200, color="Gray")

    # Удалить товар с ID 1
    delete_item(1)

    # Получить обновленный список товаров
    get_items()

	2.	Убедитесь, что библиотека requests установлена:

pip install requests


	3.	Запустите клиент:

python3 client.py

Пример вывода клиента
	•	Вывод всех товаров.
	•	Добавление нового товара.
	•	Обновление существующего товара.
	•	Удаление товара.

Автор

Kateryna