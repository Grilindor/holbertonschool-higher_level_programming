#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""


from flask import Flask, jsonify, request

app = Flask(__name__)

"""Stockage des données en mémoire"""
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    return "Bienvenue sur l'API Flask !"


@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404


@app.route('/add_user/', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({"error": "L'utilisateur existe déjà"}), 400

    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = user
    return jsonify({"message": "Utilisateur ajouté", "user": user})


if __name__ == "__main__":
    app.run()
