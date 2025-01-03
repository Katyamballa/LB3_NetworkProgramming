from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Пользовательские данные для аутентификации
users = {
    "admin": "password123",
    "user": "mypassword"
}

# Каталог товаров
catalog = {
    1: {"name": "Laptop", "price": 1000, "color": "Silver"},
    2: {"name": "Phone", "price": 500, "color": "Black"}
}

# Аутентификация
@auth.get_password
def get_password(username):
    return users.get(username)

@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

# Эндпоинт для работы с каталогом
@app.route("/items", methods=["GET", "POST"])
@auth.login_required
def items():
    if request.method == "GET":
        # Возврат всех товаров
        return jsonify(catalog)

    if request.method == "POST":
        # Добавление нового товара
        if not request.json or "name" not in request.json:
            abort(400, description="Invalid data")
        
        item_id = max(catalog.keys()) + 1 if catalog else 1
        catalog[item_id] = {
            "name": request.json["name"],
            "price": request.json.get("price", 0),
            "color": request.json.get("color", "Unknown")
        }
        return jsonify({"id": item_id, "item": catalog[item_id]}), 201

# Эндпоинт для работы с конкретным товаром
@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
@auth.login_required
def item(item_id):
    if item_id not in catalog:
        abort(404, description="Item not found")

    if request.method == "GET":
        # Возврат информации о конкретном товаре
        return jsonify(catalog[item_id])

    if request.method == "PUT":
        # Обновление товара
        if not request.json:
            abort(400, description="Invalid data")

        catalog[item_id].update({
            "name": request.json.get("name", catalog[item_id]["name"]),
            "price": request.json.get("price", catalog[item_id]["price"]),
            "color": request.json.get("color", catalog[item_id]["color"])
        })
        return jsonify({"id": item_id, "item": catalog[item_id]})

    if request.method == "DELETE":
        # Удаление товара
        del catalog[item_id]
        return jsonify({"message": "Item deleted"})

# Запуск сервера
if __name__ == "__main__":
    app.run(port=8000)