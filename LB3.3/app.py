import json
from flask import Flask, request, jsonify, abort
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Данные для аутентификации
USERS = {
    "admin": "password123"
}

# Каталог товаров
ITEMS_FILE = "items.json"

# Загрузка данных из файла
def load_items():
    try:
        with open(ITEMS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Сохранение данных в файл
def save_items(items):
    with open(ITEMS_FILE, "w") as file:
        json.dump(items, file, indent=4)

# HTTP Basic аутентификация
@auth.verify_password
def verify_password(username, password):
    if username in USERS and USERS[username] == password:
        return username
    return None

# Endpoint: Получить все товары или добавить новый
@app.route('/items', methods=['GET', 'POST'])
@auth.login_required
def items():
    if request.method == 'GET':
        items = load_items()
        return jsonify(items)

    if request.method == 'POST':
        new_item = request.json
        if not new_item.get("id") or not new_item.get("name") or not new_item.get("price"):
            return jsonify({"error": "Invalid item data"}), 400

        items = load_items()
        items.append(new_item)
        save_items(items)
        return jsonify(new_item), 201

# Endpoint: Получить, обновить или удалить товар по ID
@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def item_by_id(item_id):
    items = load_items()
    item = next((i for i in items if i["id"] == item_id), None)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    if request.method == 'GET':
        return jsonify(item)

    if request.method == 'PUT':
        updated_data = request.json
        item.update(updated_data)
        save_items(items)
        return jsonify(item)

    if request.method == 'DELETE':
        items = [i for i in items if i["id"] != item_id]
        save_items(items)
        return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(port=8000)
