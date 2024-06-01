#!/usr/bin/python3
"""Develop a Simple API using Python with Flask"""


from flask import Flask
from flask import jsonify, request

"""Dictionary containing users, with a test user jane"""
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

"""Initialize the Flask application"""
app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


"""Route to get user names as JSON"""


@app.route("/data")
def data():
    """Get the list of user names"""
    usernames = list(users.keys())
    """Return the list of user names as JSON"""
    return jsonify(usernames)


"""Route to return the status OK"""


@app.route('/status')
def status():
    return 'OK'


"""Route to return details of a specific user"""


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "Utilisateur non trouvé"}), 404


"""Route to add a new user via a POST request"""


@app.route('/add_user', methods=['POST'])
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

"""execut application Flask"""


if __name__ == "__main__":
    app.run()
